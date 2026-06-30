from __future__ import annotations

from typing import Any


def build_summary(result: dict) -> dict:
    """Placeholder dashboard summary data."""
    return {
        "particle_count": result.get("particle_count", 0),
        "average_size": result.get("average_size", 0.0),
        "mci": result.get("mci", 0.0),
        "accuracy": result.get("accuracy", 0.0),
    }


def render_chart_data(result: dict) -> list[tuple[str, float]]:
    """Placeholder chart data."""
    return [("placeholder", float(result.get("particle_count", 0)))]
