"""
Image preprocessing module for OCR optimization.
Handles grayscale conversion, thresholding, and deskewing.
"""
import cv2
import numpy as np
from typing import Tuple


def to_grayscale(image: np.ndarray) -> np.ndarray:
    """Convert image to grayscale if it's color."""
    if len(image.shape) == 3:
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return image


def apply_threshold(image: np.ndarray) -> np.ndarray:
    """Apply adaptive thresholding for better OCR results."""
    # Use adaptive thresholding for varying lighting conditions
    return cv2.adaptiveThreshold(
        image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
    )


def detect_skew_angle(image: np.ndarray) -> float:
    """Detect skew angle in degrees using Hough transform."""
    # Edge detection
    edges = cv2.Canny(image, 50, 150, apertureSize=3)
    
    # Hough line detection
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
    
    if lines is None or len(lines) == 0:
        return 0.0
    
    # Calculate angles
    angles = []
    for line in lines[:20]:  # Check first 20 lines
        rho, theta = line[0]
        angle = (theta * 180 / np.pi) - 90
        if -45 < angle < 45:
            angles.append(angle)
    
    if not angles:
        return 0.0
    
    # Return median angle
    return np.median(angles)


def deskew(image: np.ndarray, angle: float) -> np.ndarray:
    """Rotate image to correct skew if angle is significant."""
    if abs(angle) < 0.5:  # Skip if angle is too small
        return image
    
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    
    # Rotation matrix
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    
    # Rotate image
    rotated = cv2.warpAffine(
        image, M, (w, h),
        flags=cv2.INTER_CUBIC,
        borderMode=cv2.BORDER_REPLICATE
    )
    
    return rotated


def preprocess_image(image: np.ndarray) -> np.ndarray:
    """
    Complete preprocessing pipeline:
    1. Convert to grayscale
    2. Detect and correct skew
    3. Apply thresholding
    
    Args:
        image: Input image as numpy array
        
    Returns:
        Preprocessed image ready for OCR
    """
    # Step 1: Grayscale
    gray = to_grayscale(image)
    
    # Step 2: Deskew
    angle = detect_skew_angle(gray)
    if abs(angle) > 0.5:
        gray = deskew(gray, angle)
    
    # Step 3: Threshold
    thresholded = apply_threshold(gray)
    
    return thresholded
