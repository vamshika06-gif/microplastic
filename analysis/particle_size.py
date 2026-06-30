from __future__ import annotations


def estimate_particle_sizes(detections: list[dict]) -> list[float]:
    """Return placeholder size estimates in micrometers."""
    return [round(12.5 + index * 2.4, 2) for index in range(len(detections))]
