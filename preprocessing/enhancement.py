from __future__ import annotations

from PIL import Image, ImageOps


def enhance_image(image: Image.Image) -> Image.Image:
    """Apply a simple enhancement pipeline for visualization."""
    image = ImageOps.autocontrast(image)
    return image
