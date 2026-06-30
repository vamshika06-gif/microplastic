from __future__ import annotations

from typing import Any


def load_cnn_model(model_path: str | None = None) -> dict[str, Any]:
    """Return a placeholder CNN model descriptor until real weights are available."""
    return {"name": "CNN Baseline", "path": model_path or "Not provided", "ready": False}


def predict_class(image: Any, model: dict[str, Any] | None = None) -> str:
    """Return a placeholder class label when no trained model exists."""
    if model is None:
        model = load_cnn_model()
    return "microplastic-fragment"
