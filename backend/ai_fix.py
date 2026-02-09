"""
LLM-based text correction module using llama.cpp.
Fixes OCR errors and converts to formal Mongolian office language.
"""
import subprocess
import json
import tempfile
import os
from typing import Optional


class LLMCorrector:
    """Offline LLM text corrector using llama.cpp."""
    
    def __init__(self, model_path: Optional[str] = None):
        """
        Initialize LLM corrector.
        
        Args:
            model_path: Path to llama.cpp model file (.gguf)
                       If None, will look for default model
        """
        self.model_path = model_path or self._find_model()
        self.llama_cpp_path = self._find_llama_cpp()
    
    def _find_model(self) -> str:
        """Find default model file in models directory."""
        models_dir = os.path.join(os.path.dirname(__file__), "models")
        if os.path.exists(models_dir):
            for file in os.listdir(models_dir):
                if file.endswith(".gguf"):
                    model_path = os.path.join(models_dir, file)
                    # Return absolute path
                    return os.path.abspath(model_path)
        
        # Default fallback - try config path
        from config import MODEL_PATH
        if MODEL_PATH and os.path.exists(MODEL_PATH):
            return str(MODEL_PATH)
        
        # Last fallback
        default_path = os.path.join(os.path.dirname(__file__), "models", "mongolian.gguf")
        return os.path.abspath(default_path)
    
    def _find_llama_cpp(self) -> str:
        """Find llama.cpp executable."""
        # Check common locations and executable names
        possible_paths = [
            os.path.join(os.path.dirname(__file__), "llama.cpp", "main.exe"),
            os.path.join(os.path.dirname(__file__), "llama.cpp", "llama-cli.exe"),
            "llama.cpp/main.exe",
            "llama.cpp/llama-cli.exe",
            "llama-cpp/main.exe",
            "llama-cpp/llama-cli.exe",
            "main.exe",  # If in PATH
            "llama-cli.exe"  # If in PATH
        ]
        
        for path in possible_paths:
            if os.path.exists(path) or self._check_command(path):
                return path
        
        return "llama-cli"  # Fallback to PATH
    
    def _check_command(self, cmd: str) -> bool:
        """Check if command exists."""
        try:
            subprocess.run([cmd, "--help"], 
                         capture_output=True, 
                         timeout=2)
            return True
        except:
            return False
    
    def _create_prompt(self, raw_text: str) -> str:
        """Create prompt for LLM correction."""
        prompt = f"""Танд доорх OCR-аар олж авсан монгол бичвэр байна. Дараах ажлуудыг хий:
1. OCR-ийн алдааг засах
2. Анхны утгыг хадгалах
3. Албан ёсны оффис хэлбэрт шилжүүлэх

OCR текст:
{raw_text}

Зассан текст:"""
        return prompt
    
    def correct_text(self, raw_text: str, max_tokens: int = 2000) -> str:
        """
        Correct OCR text using offline LLM.
        
        Args:
            raw_text: Raw OCR output text
            max_tokens: Maximum tokens to generate
            
        Returns:
            Corrected text
        """
        if not raw_text.strip():
            return raw_text
        
        # Check if model and llama.cpp exist
        model_exists = os.path.exists(self.model_path)
        llama_exists = os.path.exists(self.llama_cpp_path)
        
        if not model_exists:
            print(f"Warning: Model not found at {self.model_path}")
            return raw_text
        
        if not llama_exists:
            print(f"Warning: llama.cpp not found at {self.llama_cpp_path}")
            return raw_text
        
        print(f"Using LLM: model={self.model_path}, llama={self.llama_cpp_path}")
        
        try:
            prompt = self._create_prompt(raw_text)
            
            # Create temporary prompt file
            with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', 
                                           suffix='.txt', delete=False) as f:
                f.write(prompt)
                prompt_file = f.name
            
            try:
                # Call llama.cpp with file input
                cmd = [
                    self.llama_cpp_path,
                    "-m", self.model_path,
                    "-f", prompt_file,
                    "-n", str(max_tokens),
                    "--temp", "0.7",
                    "--top-p", "0.9",
                    "--repeat-penalty", "1.1",
                    "--no-penalize-nl"
                ]
                
                print(f"Running LLM: {os.path.basename(self.llama_cpp_path)} with model {os.path.basename(self.model_path)}")
                
                result = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    encoding='utf-8',
                    errors='replace',
                    timeout=300,
                    cwd=os.path.dirname(self.llama_cpp_path) if os.path.dirname(self.llama_cpp_path) else None,
                    shell=False
                )
                
                if result.returncode == 0:
                    # Extract corrected text from output
                    output = result.stdout.strip()
                    
                    # Remove prompt from output if present
                    if "Зассан текст:" in output:
                        corrected = output.split("Зассан текст:")[-1].strip()
                    else:
                        # Try to find the corrected text after the prompt
                        lines = output.split('\n')
                        # Skip prompt lines and get the actual response
                        corrected = '\n'.join([line for line in lines if line.strip() and not line.startswith('OCR текст:') and not line.startswith('Танд доорх')])
                        if not corrected:
                            corrected = output
                    
                    corrected = corrected.strip()
                    if corrected and corrected != raw_text:
                        print(f"LLM correction successful: {len(corrected)} chars")
                        return corrected
                    else:
                        print("LLM returned same or empty text, using original")
                        return raw_text
                else:
                    error_msg = result.stderr if result.stderr else "Unknown error"
                    print(f"LLM error (code {result.returncode}): {error_msg[:200]}")
                    if result.stdout:
                        print(f"LLM stdout: {result.stdout[:200]}")
                    return raw_text
                    
            finally:
                # Clean up prompt file
                if os.path.exists(prompt_file):
                    os.unlink(prompt_file)
                
        except subprocess.TimeoutExpired:
            print("LLM correction timed out")
            return raw_text
        except Exception as e:
            print(f"LLM correction error: {str(e)}")
            return raw_text
    
    def correct_text_simple(self, raw_text: str) -> str:
        """
        Simple fallback correction without LLM.
        Basic cleanup and formatting.
        """
        if not raw_text.strip():
            return raw_text
        
        # Basic cleanup
        lines = raw_text.split('\n')
        corrected_lines = []
        
        for line in lines:
            line = line.strip()
            if line:
                # Remove excessive spaces
                line = ' '.join(line.split())
                corrected_lines.append(line)
        
        return '\n'.join(corrected_lines)
