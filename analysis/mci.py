from __future__ import annotations


def calculate_mci(particle_count: int, average_size: float) -> float:
    """Compute a lightweight placeholder contamination index."""
    return round(min(100.0, particle_count * 1.8 + average_size * 0.7), 2)
