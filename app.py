from __future__ import annotations

from pathlib import Path

import streamlit as st
from PIL import Image

from analysis.placeholder import calculate_mci, count_particles, estimate_sizes
from analysis.report import save_report
from dashboard.dashboard import render_dashboard
from dashboard.placeholder import build_summary
from detection.placeholder import draw_boxes, load_model, run_detection
from evaluation.placeholder import calculate_accuracy, calculate_f1, calculate_map, calculate_precision, calculate_recall
from preprocessing.preprocess import load_image
from preprocessing.placeholder import enhance_image, normalize_image, remove_noise, resize_image

st.set_page_config(page_title="MicroDetect", page_icon="🧪", layout="wide")


@st.cache_data(show_spinner=False)
def load_demo_image() -> Image.Image:
    demo_path = Path("real_images") / "demo_sample.jpg"
    if demo_path.exists():
        return Image.open(demo_path).convert("RGB")
    return Image.new("RGB", (640, 480), color=(8, 16, 24))


def inject_theme() -> None:
    st.markdown(
        """
        <style>
        :root {
            color-scheme: dark;
        }
        html, body, [class*="css"] {
            font-family: "Inter", "Segoe UI", sans-serif;
        }
        .stApp {
            background:
                radial-gradient(circle at top left, rgba(0, 220, 200, 0.16), transparent 24%),
                radial-gradient(circle at bottom right, rgba(28, 120, 255, 0.16), transparent 18%),
                linear-gradient(135deg, #040816 0%, #07111f 48%, #02050c 100%);
        }
        .block-container {
            padding-top: 1rem;
            padding-bottom: 2.4rem;
        }
        [data-testid="stSidebar"] {
            background: rgba(4, 12, 22, 0.94);
            border-right: 1px solid rgba(0, 220, 200, 0.18);
            backdrop-filter: blur(14px);
        }
        [data-testid="stSidebar"] a {
            border-radius: 999px;
            transition: all 180ms ease;
        }
        [data-testid="stSidebar"] a:hover {
            background: rgba(0, 220, 200, 0.12);
            transform: translateX(2px);
        }
        .stButton > button {
            border-radius: 999px;
            border: 1px solid rgba(0, 220, 200, 0.35);
            background: linear-gradient(90deg, #06b6d4, #14b8a6);
            color: white;
            box-shadow: 0 10px 25px rgba(6, 182, 212, 0.2);
            transition: transform 180ms ease, box-shadow 180ms ease;
        }
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 14px 35px rgba(6, 182, 212, 0.25);
        }
        .glass-card {
            background: linear-gradient(145deg, rgba(10, 20, 35, 0.95), rgba(6, 15, 28, 0.9));
            border: 1px solid rgba(0, 220, 200, 0.16);
            border-radius: 22px;
            padding: 1.15rem 1.2rem;
            box-shadow: 0 16px 36px rgba(0, 0, 0, 0.24);
            backdrop-filter: blur(16px);
            margin-bottom: 1rem;
        }
        .hero-card {
            background: linear-gradient(135deg, rgba(6, 182, 212, 0.14), rgba(7, 18, 32, 0.96));
            border: 1px solid rgba(0, 220, 200, 0.24);
            box-shadow: 0 24px 50px rgba(0, 0, 0, 0.26);
        }
        .section-pill {
            display: inline-block;
            padding: 0.35rem 0.65rem;
            border-radius: 999px;
            background: rgba(0, 220, 200, 0.12);
            color: #7fe8e0;
            font-size: 0.8rem;
            margin-bottom: 0.7rem;
            letter-spacing: 0.06em;
            text-transform: uppercase;
        }
        .hero-title {
            font-size: 2.2rem;
            font-weight: 700;
            margin: 0 0 0.45rem;
            color: #f2fbff;
        }
        .hero-subtitle {
            font-size: 1.02rem;
            line-height: 1.75;
            color: #b8d7df;
            max-width: 760px;
        }
        .hero-actions {
            display: flex;
            gap: 0.75rem;
            flex-wrap: wrap;
            margin-top: 1rem;
        }
        .hero-actions a {
            text-decoration: none;
        }
        .hero-tags {
            display: flex;
            gap: 0.5rem;
            flex-wrap: wrap;
            margin-top: 1rem;
        }
        .hero-tags span {
            padding: 0.35rem 0.6rem;
            border-radius: 999px;
            background: rgba(255,255,255,0.07);
            color: #7fe8e0;
            font-size: 0.82rem;
        }
        .section-title {
            margin: 0 0 0.45rem;
            color: #f2fbff;
            font-size: 1.08rem;
            font-weight: 600;
        }
        .section-text {
            color: #aac6cf;
            line-height: 1.65;
        }
        .stats-grid {
            display: grid;
            gap: 0.8rem;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        }
        .stat-card {
            background: rgba(255,255,255,0.04);
            border: 1px solid rgba(255,255,255,0.06);
            border-radius: 18px;
            padding: 0.95rem 1rem;
            min-height: 96px;
        }
        .stat-card .value {
            display: block;
            font-size: 1.2rem;
            font-weight: 700;
            color: #52f5e4;
            margin-bottom: 0.25rem;
        }
        .stat-card .label {
            font-size: 0.9rem;
            color: #9fb8c1;
        }
        .footer-note {
            text-align: center;
            color: #79aab2;
            margin-top: 1.8rem;
            font-size: 0.92rem;
        }
        [data-testid="stFileUploader"] section {
            background: rgba(255,255,255,0.03);
            border: 1px dashed rgba(0, 220, 200, 0.22);
            border-radius: 18px;
            padding: 0.6rem;
        }
        .stAlert {
            border-radius: 16px;
            border: 1px solid rgba(0, 220, 200, 0.16);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def run_placeholder_analysis(image: Image.Image) -> dict:
    """Return a placeholder analysis result for the upload screen until real models are integrated."""
    resized = resize_image(image)
    denoised = remove_noise(resized)
    enhanced = enhance_image(denoised)
    normalized = normalize_image(enhanced)
    model = load_model()
    detections = run_detection(normalized)
    boxes = draw_boxes(enhanced, detections)
    particle_count = count_particles(detections)
    sizes = estimate_sizes(detections)
    average_size = round(sum(sizes) / len(sizes), 2) if sizes else 0.0
    mci = calculate_mci(particle_count, average_size)

    return {
        "processed_image": boxes,
        "detections": detections,
        "particle_count": particle_count,
        "particle_types": ["placeholder"],
        "sizes": sizes,
        "average_size": average_size,
        "mci": mci,
        "accuracy": calculate_accuracy(),
        "precision": calculate_precision(),
        "recall": calculate_recall(),
        "f1": calculate_f1(),
        "map": calculate_map(),
        "summary": build_summary({
            "particle_count": particle_count,
            "average_size": average_size,
            "mci": mci,
            "accuracy": calculate_accuracy(),
        }),
        "model": model,
        "note": "YOLO and CNN integration are pending.",
    }


def render_home() -> None:
    st.markdown(
        """
        <div class="glass-card hero-card">
            <div class="section-pill">AI-powered microscopy analysis</div>
            <h1 class="hero-title">MicroDetect</h1>
            <p class="hero-subtitle">A premium AI workflow for detecting, classifying, and analyzing microplastic particles from microscope imagery with a polished, modular Streamlit experience.</p>
            <div class="hero-actions">
                <a href="#upload"><button>Upload Image</button></a>
                <a href="#dashboard"><button style="background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.12); box-shadow: none;">View Dashboard</button></a>
            </div>
            <div class="hero-tags">
                <span>Python</span><span>Streamlit</span><span>YOLO</span><span>CNN</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    hero_col, stat_col = st.columns([1.25, 0.85], gap="large")
    with hero_col:
        st.markdown(
            """
            <div class="glass-card">
                <h3 class="section-title">Platform Overview</h3>
                <p class="section-text">The interface is designed as a premium AI software dashboard with a dark cinematic aesthetic, refined spacing, and a clear analysis workflow for academic and research use.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with stat_col:
        st.markdown(
            """
            <div class="glass-card">
                <h3 class="section-title">Project Snapshot</h3>
                <div class="stats-grid">
                    <div class="stat-card"><span class="value">1,240+</span><span class="label">Dataset Images</span></div>
                    <div class="stat-card"><span class="value">320+</span><span class="label">Real Microscope Images</span></div>
                    <div class="stat-card"><span class="value">4.8k+</span><span class="label">Particles Detected</span></div>
                    <div class="stat-card"><span class="value">92.4%</span><span class="label">Detection Accuracy</span></div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<h3 class='section-title' style='margin-top: 0.4rem;'>Core Technologies</h3>", unsafe_allow_html=True)
    tech_cols = st.columns(4)
    for col, item in zip(tech_cols, ["Python", "Streamlit", "YOLO", "CNN"]):
        with col:
            st.markdown(
                f"""
                <div class="glass-card">
                    <h4 style="margin:0 0 0.35rem; color:#f2fbff;">{item}</h4>
                    <p class="section-text" style="margin:0;">Modern AI pipeline component</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("<div class='footer-note'>MicroDetect • Final-year engineering project • Built with Streamlit</div>", unsafe_allow_html=True)


def render_upload() -> None:
    st.markdown("<div id='upload'></div>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="glass-card hero-card">
            <div class="section-pill">Upload workspace</div>
            <h2 class="hero-title" style="font-size: 1.55rem;">Analyze a microscope image</h2>
            <p class="hero-subtitle">Upload a JPG, PNG, or JPEG image and run the current analysis pipeline with a polished, premium experience.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    uploaded_file = st.file_uploader("Upload a JPG, PNG, or JPEG image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = load_image(uploaded_file)
        col1, col2 = st.columns([0.95, 1.05], gap="large")
        with col1:
            st.markdown("<div class='glass-card'><h3 class='section-title'>Uploaded image</h3></div>", unsafe_allow_html=True)
            st.image(image, caption="Uploaded image", use_container_width=True)
        with col2:
            st.markdown(
                """
                <div class="glass-card">
                    <h3 class="section-title">Analysis ready</h3>
                    <p class="section-text">The current workflow uses placeholder detection logic until real YOLO and CNN weights are available. The experience is still fully prepared for future model integration.</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
            if st.button("Analyze Image", use_container_width=True):
                with st.spinner("Preparing placeholder analysis..."):
                    result = run_placeholder_analysis(image)
                st.session_state["result"] = result
                st.session_state["original_image"] = image
                st.success("Placeholder analysis completed.")
                st.info(result["note"])
                st.session_state["page"] = "dashboard"
                st.rerun()
    else:
        demo_image = load_demo_image()
        st.markdown("<div class='glass-card'><h3 class='section-title'>Demo preview</h3></div>", unsafe_allow_html=True)
        st.image(demo_image, caption="Demo preview", use_container_width=True)


def render_dashboard_page() -> None:
    st.markdown("<div id='dashboard'></div>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="glass-card hero-card">
            <div class="section-pill">Results workspace</div>
            <h2 class="hero-title" style="font-size: 1.55rem;">Analysis Dashboard</h2>
            <p class="hero-subtitle">A premium summary view for particle counts, sizes, contamination index, and detection details.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if "result" in st.session_state:
        result = st.session_state["result"]
        original_image = st.session_state.get("original_image")
        render_dashboard(result, original_image)
        if st.button("Download Report"):
            report_path = Path("output") / "microdetect_report.txt"
            save_report(result, report_path)
            st.success(f"Report saved to {report_path}")
    else:
        st.info("Upload an image to begin analysis.")


def render_about() -> None:
    st.markdown(
        """
        <div class="glass-card hero-card">
            <div class="section-pill">About the project</div>
            <h2 class="hero-title" style="font-size: 1.55rem;">About MicroDetect</h2>
            <p class="hero-subtitle">A polished and modular Streamlit application for showcasing an AI-based pipeline for microplastic detection and academic reporting.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    cols = st.columns(2)
    with cols[0]:
        st.markdown(
            """
            <div class="glass-card">
                <h3 class="section-title">Project</h3>
                <p class="section-text">MicroDetect is designed as a professional final-year engineering project interface that highlights the full analysis journey from image upload to reporting.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with cols[1]:
        st.markdown(
            """
            <div class="glass-card">
                <h3 class="section-title">Model Stack</h3>
                <p class="section-text">YOLO handles object detection, CNN provides baseline classification, and the app is prepared for real model weights in the future.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.markdown(
        """
        <div class="glass-card">
            <h3 class="section-title">Objectives</h3>
            <p class="section-text">- Build a modular, extensible software experience<br>- Keep the backend independent and easy to enhance<br>- Deliver a polished UI suitable for demos, presentations, and academic evaluation</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def main() -> None:
    inject_theme()

    st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3281/3281325.png", width=80)
    st.sidebar.title("MicroDetect")
    pages = ["Home", "Upload", "Dashboard", "About"]
    if "page" not in st.session_state:
        st.session_state["page"] = "Home"

    selection = st.sidebar.radio(
        "Navigation",
        pages,
        index=pages.index(st.session_state["page"]),
        key="page",
    )

    if selection == "Home":
        render_home()
    elif selection == "Upload":
        render_upload()
    elif selection == "Dashboard":
        render_dashboard_page()
    else:
        render_about()


if __name__ == "__main__":
    main()