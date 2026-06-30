from __future__ import annotations

from PIL import Image, ImageFilter


def remove_noise(image: Image.Image) -> Image.Image:
    """Apply a light smoothing pass as a placeholder noise removal step."""
    return image.filter(ImageFilter.GaussianBlur(radius=0.5))
