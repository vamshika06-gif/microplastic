from __future__ import annotations

import streamlit as st
from PIL import Image


def render_dashboard(result: dict, original_image: Image.Image | None = None) -> None:
    """Render the main analysis dashboard cards."""
    st.markdown(
        """
        <div class="glass-card">
            <h3 class="section-title">Detection summary</h3>
            <div class="stats-grid">
                <div class="stat-card"><span class="value">{particles}</span><span class="label">Particles</span></div>
                <div class="stat-card"><span class="value">{types}</span><span class="label">Particle Types</span></div>
                <div class="stat-card"><span class="value">{size} µm</span><span class="label">Average Size</span></div>
                <div class="stat-card"><span class="value">{mci}</span><span class="label">MCI</span></div>
            </div>
        </div>
        """.format(
            particles=result.get("particle_count", 0),
            types=len(result.get("particle_types", [])),
            size=result.get("average_size", 0.0),
            mci=result.get("mci", 0.0),
        ),
        unsafe_allow_html=True,
    )

    if original_image is not None:
        st.markdown("<div class='glass-card'><h3 class='section-title'>Preview</h3></div>", unsafe_allow_html=True)
        col_left, col_right = st.columns(2)
        with col_left:
            st.image(original_image, caption="Original image", use_container_width=True)
        with col_right:
            st.image(result.get("processed_image", original_image), caption="Detected preview", use_container_width=True)

    st.markdown("<div class='glass-card'><h3 class='section-title'>Detection details</h3></div>", unsafe_allow_html=True)
    st.dataframe(
        {
            "Particle": [f"P{i + 1}" for i in range(len(result.get("detections", [])))],
            "Type": result.get("particle_types", []),
            "Confidence": [d.get("confidence", 0.0) for d in result.get("detections", [])],
            "Size (µm)": result.get("sizes", []),
        }
    )
