"""
FastAPI backend server for PDF to Word.
Handles file upload, OCR, LLM correction, and Word export.
"""
from fastapi import FastAPI, UploadFile, File, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
import uvicorn
import os
import tempfile
import shutil
from pathlib import Path

from preprocess import preprocess_image
from ocr import process_file, ocr_image
from ai_fix import LLMCorrector
from export import export_to_word

app = FastAPI(title="PDF to Word API")

# CORS middleware for Electron frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize LLM corrector
llm_corrector = LLMCorrector()

# Temporary directory for uploads
UPLOAD_DIR = Path("temp_uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


class ExportRequest(BaseModel):
    """Request model for export endpoint."""
    text: str


@app.get("/")
def root():
    """Health check endpoint."""
    return {"status": "ok", "message": "PDF to Word API"}


@app.get("/status")
def get_status():
    """Get LLM configuration status."""
    import os
    from ai_fix import LLMCorrector
    
    corrector = LLMCorrector()
    llama_exists = os.path.exists(corrector.llama_cpp_path)
    model_exists = os.path.exists(corrector.model_path)
    
    return {
        "llama_available": llama_exists,
        "model_available": model_exists,
        "llm_ready": llama_exists and model_exists,
        "llama_path": str(corrector.llama_cpp_path),
        "model_path": str(corrector.model_path)
    }


@app.post("/process")
async def process_document(file: UploadFile = File(...)):
    """
    Process uploaded document:
    1. Save file temporarily
    2. Determine if PDF or image
    3. Extract text (direct or OCR)
    4. Preprocess images if needed
    5. Run OCR with Mongolian support
    6. Correct text with LLM
    7. Return corrected text
    """
    try:
        # Determine file type
        is_pdf = file.filename.lower().endswith('.pdf')
        is_image = file.filename.lower().endswith(('.png', '.jpg', '.jpeg'))
        
        if not (is_pdf or is_image):
            raise HTTPException(
                status_code=400,
                detail="Unsupported file type. Please upload PDF, PNG, or JPG."
            )
        
        # Save uploaded file temporarily
        suffix = Path(file.filename).suffix
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp_file:
            shutil.copyfileobj(file.file, tmp_file)
            tmp_path = tmp_file.name
        
        try:
            # Step 1: Extract text
            raw_text = ""
            
            if is_pdf:
                # Process PDF
                from ocr import extract_text_from_pdf, pdf_to_images
                import cv2
                import numpy as np
                
                # Try text extraction first
                text, is_text_based = extract_text_from_pdf(tmp_path)
                
                if is_text_based:
                    raw_text = text
                else:
                    # Scanned PDF: convert to images, preprocess, then OCR
                    images = pdf_to_images(tmp_path)
                    texts = []
                    
                    for img in images:
                        # Preprocess image
                        preprocessed = preprocess_image(img)
                        # OCR
                        text = ocr_image(preprocessed, lang="mon+eng")
                        if text:
                            texts.append(text)
                    
                    raw_text = '\n\n'.join(texts)
            else:
                # Process image: preprocess then OCR
                import cv2
                import numpy as np
                
                image = cv2.imread(tmp_path)
                if image is None:
                    raise HTTPException(status_code=400, detail="Failed to load image")
                
                # Preprocess image
                preprocessed = preprocess_image(image)
                
                # OCR
                raw_text = ocr_image(preprocessed, lang="mon+eng")
            
            if not raw_text.strip():
                return {
                    "success": False,
                    "error": "No text extracted from document",
                    "corrected_text": ""
                }
            
            # Step 2: LLM correction
            import os
            # Check if both model and llama.cpp exist
            model_exists = os.path.exists(llm_corrector.model_path)
            llama_exists = os.path.exists(llm_corrector.llama_cpp_path)
            using_llm = model_exists and llama_exists
            
            print(f"DEBUG: Model path: {llm_corrector.model_path}")
            print(f"DEBUG: Model exists: {model_exists}")
            print(f"DEBUG: llama.cpp path: {llm_corrector.llama_cpp_path}")
            print(f"DEBUG: llama.cpp exists: {llama_exists}")
            print(f"DEBUG: Using LLM: {using_llm}")
            
            try:
                if using_llm:
                    print("Using LLM for text correction...")
                    corrected_text = llm_corrector.correct_text(raw_text)
                    if corrected_text == raw_text:
                        print("Warning: LLM returned original text, might have failed")
                else:
                    print("LLM not available, using simple correction...")
                    # Fallback to simple correction if LLM not available
                    corrected_text = llm_corrector.correct_text_simple(raw_text)
            except Exception as e:
                print(f"LLM correction failed: {e}")
                import traceback
                traceback.print_exc()
                # Fallback to simple correction
                corrected_text = llm_corrector.correct_text_simple(raw_text)
                using_llm = False
            
            return {
                "success": True,
                "raw_text": raw_text,
                "corrected_text": corrected_text,
                "used_llm": using_llm
            }
            
        finally:
            # Clean up temporary file
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
                
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Processing error: {str(e)}")


@app.post("/export")
async def export_document(request: ExportRequest):
    """
    Export corrected text to Word document.
    
    Args:
        request: ExportRequest with text field
    """
    try:
        # Create temporary Word file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.docx') as tmp_file:
            output_path = tmp_file.name
        
        # Export to Word
        export_to_word(request.text, output_path)
        
        # Return file
        return FileResponse(
            output_path,
            media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            filename="corrected_text.docx",
            background=lambda: os.unlink(output_path)  # Clean up after sending
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Export error: {str(e)}")


if __name__ == "__main__":
    # Run server on localhost:8000
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
