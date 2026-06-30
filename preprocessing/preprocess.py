from __future__ import annotations

from io import BytesIO
from typing import Tuple

import numpy as np
from PIL import Image, ImageOps


def load_image(uploaded_file) -> Image.Image:
    """Load an uploaded image into a PIL image object."""
    image = Image.open(uploaded_file).convert("RGB")
    return image


def preprocess_image(image: Image.Image, target_size: Tuple[int, int] = (640, 640)) -> np.ndarray:
    """Return a lightweight preprocessed image array for the pipeline."""
    image = ImageOps.exif_transpose(image)
    image = image.resize(target_size)
    image = ImageOps.autocontrast(image)
    arr = np.array(image, dtype=np.float32) / 255.0
    return arr


def enhance_image(image: Image.Image) -> Image.Image:
    """Apply a placeholder enhancement step."""
    return ImageOps.autocontrast(image)


def remove_noise(image: Image.Image) -> Image.Image:
    """Apply a placeholder noise-removal step."""
    return image.filter(ImageFilter.GaussianBlur(radius=0.4))


def normalize_image(image: Image.Image) -> np.ndarray:
    """Normalize image pixel values to the range [0, 1]."""
    arr = np.array(image, dtype=np.float32) / 255.0
    return arr


from PIL import ImageFilter
