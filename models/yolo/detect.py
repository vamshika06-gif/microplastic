from __future__ import annotations

from typing import Any


def load_yolo_model(model_path: str | None = None) -> dict[str, Any]:
    """Return a placeholder model descriptor until real weights are available."""
    return {"name": "YOLOv26 Placeholder", "path": model_path or "Not provided", "ready": False}


def run_detection(image: Any, model: dict[str, Any] | None = None) -> list[dict]:
    """Return simulated detection results when weights are unavailable."""
    if model is None:
        model = load_yolo_model()

    detections = [
        {"box": [80, 90, 220, 210], "label": "microplastic", "confidence": 0.91},
        {"box": [260, 140, 380, 260], "label": "fragment", "confidence": 0.87},
    ]
    return detections


def draw_boxes(image: Any, detections: list[dict]) -> Any:
    """Return the original image as a placeholder; real drawing can be added later."""
    return image
