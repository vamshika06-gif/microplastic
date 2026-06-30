from __future__ import annotations

from PIL import Image


def resize_image(image: Image.Image, size: tuple[int, int] = (640, 640)) -> Image.Image:
    """Resize an image to a consistent target size."""
    return image.resize(size)
