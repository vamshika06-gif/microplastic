from __future__ import annotations

from typing import Any


def load_model() -> dict:
    """Placeholder model loader returning dummy metadata."""
    return {"name": "placeholder-model", "status": "not-trained"}


def run_detection(image: Any) -> list[dict]:
    """Placeholder detection returning an empty list."""
    return []


def draw_boxes(image: Any, detections: list[dict]) -> Any:
    """Placeholder bounding-box renderer returning the image unchanged."""
    return image
