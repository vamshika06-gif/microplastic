from __future__ import annotations

from typing import Any


def count_particles(detections: list[dict]) -> int:
    """Placeholder particle count function."""
    return len(detections)


def estimate_sizes(detections: list[dict]) -> list[float]:
    """Placeholder size estimates returning dummy values."""
    return [0.0 for _ in detections]


def calculate_mci(particle_count: int, average_size: float) -> float:
    """Placeholder contamination index calculation."""
    return round(particle_count * 0.1 + average_size * 0.05, 2)
