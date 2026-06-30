from __future__ import annotations

import pandas as pd


def build_summary_dataframe(result: dict) -> pd.DataFrame:
    """Create a small summary table for the dashboard."""
    return pd.DataFrame(
        {
            "Metric": ["Particle Count", "Average Size (µm)", "MCI", "Accuracy"],
            "Value": [result.get("particle_count", 0), result.get("average_size", 0.0), result.get("mci", 0.0), result.get("accuracy", 0.0)],
        }
    )
