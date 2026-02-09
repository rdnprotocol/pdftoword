"""
OCR module using Tesseract with Mongolian Cyrillic support.
Handles both text-based PDF extraction and image OCR.
"""
import pytesseract
from PIL import Image
import pdf2image
import io
from typing import List, Tuple
import numpy as np
import cv2
from config import configure_tesseract, configure_poppler

# Configure paths
configure_tesseract()
configure_poppler()


def extract_text_from_pdf(pdf_path: str) -> Tuple[str, bool]:
    """
    Extract text from PDF.
    
    Returns:
        Tuple of (text, is_text_based)
        - If text-based PDF: returns extracted text directly
        - If scanned PDF: returns empty string and False
    """
    try:
        # Try direct text extraction first
        import PyPDF2
        
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text_content = []
            
            for page in pdf_reader.pages:
                text = page.extract_text()
                if text.strip():
                    text_content.append(text)
            
            if text_content:
                return '\n\n'.join(text_content), True
    except Exception:
        pass
    
    # If direct extraction failed, it's likely a scanned PDF
    return "", False


def pdf_to_images(pdf_path: str) -> List[np.ndarray]:
    """Convert PDF pages to images for OCR."""
    try:
        images = pdf2image.convert_from_path(pdf_path, dpi=300)
        return [np.array(img) for img in images]
    except Exception as e:
        raise Exception(f"Failed to convert PDF to images: {str(e)}")


def ocr_image(image: np.ndarray, lang: str = "mon+eng") -> str:
    """
    Perform OCR on a single image.
    
    Args:
        image: Image as numpy array (already preprocessed)
        lang: Tesseract language code (mon+eng for Mongolian + English)
        
    Returns:
        Extracted text string
    """
    # Convert numpy array to PIL Image
    if isinstance(image, np.ndarray):
        pil_image = Image.fromarray(image)
    else:
        pil_image = image
    
    # Configure Tesseract for Mongolian Cyrillic
    custom_config = r'--oem 3 --psm 6'
    
    # Perform OCR
    text = pytesseract.image_to_string(
        pil_image,
        lang=lang,
        config=custom_config
    )
    
    return text.strip()


def process_file(file_path: str, is_pdf: bool = False) -> str:
    """
    Main function to process uploaded file.
    
    Args:
        file_path: Path to uploaded file
        is_pdf: Whether file is PDF
        
    Returns:
        Extracted raw text
    """
    if is_pdf:
        # Try text extraction first
        text, is_text_based = extract_text_from_pdf(file_path)
        
        if is_text_based:
            return text
        
        # If scanned PDF, convert to images and OCR
        images = pdf_to_images(file_path)
        texts = []
        
        for img in images:
            # Preprocess will be done in main.py before calling OCR
            text = ocr_image(img, lang="mon+eng")
            if text:
                texts.append(text)
        
        return '\n\n'.join(texts)
    
    else:
        # Image file - load and OCR
        image = cv2.imread(file_path)
        if image is None:
            raise Exception(f"Failed to load image: {file_path}")
        
        # Preprocess will be done in main.py before calling OCR
        return ocr_image(image, lang="mon+eng")
