from __future__ import annotations

from pathlib import Path


def build_report(result: dict) -> str:
    """Create a simple plain-text report for downloaded results."""
    lines = [
        "MicroDetect Analysis Report",
        "==========================",
        f"Particle Count: {result.get('particle_count', 0)}",
        f"Particle Types: {', '.join(result.get('particle_types', [])) or 'N/A'}",
        f"Average Size (µm): {result.get('average_size', 0.0)}",
        f"MCI: {result.get('mci', 0.0)}",
        f"Accuracy: {result.get('accuracy', 0.0)}%",
    ]
    return "\n".join(lines)


def save_report(result: dict, path: str | Path) -> None:
    """Save the generated report to disk."""
    path = Path(path)
    path.write_text(build_report(result), encoding="utf-8")
