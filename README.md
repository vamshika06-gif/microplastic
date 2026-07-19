# Deep Learning-Based Automated Microplastic Detection and Classification System Using Microscopic Image Analysis

## Overview
This project uses deep learning techniques to automatically detect and classify microplastics from microscopic images. It aims to reduce manual effort, improve detection accuracy, and support environmental monitoring and research.

## Features
- Image preprocessing
- CNN-based microplastic classification
- YOLOv8-based microplastic detection
- Dataset organization and augmentation
- Model evaluation using standard metrics
- Visualization of detection results

## Tech Stack
- Python
- TensorFlow / Keras
- YOLOv8 (Ultralytics)
- OpenCV
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- Jupyter Notebook

## Project Structure

```
microplastic/
│── dataset/
│── models/
│── notebooks/
│── src/
│── results/
│── requirements.txt
│── README.md
```

## Dataset
The project uses microscopic images of microplastics collected from publicly available datasets and/or custom datasets.

### Classes
- Fiber
- Fragment
- Film
- Pellet
- Foam

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/microplastic.git
cd microplastic
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Train the CNN model:

```bash
python train_cnn.py
```

Run YOLOv8 detection:

```bash
python detect.py
```

Evaluate the model:

```bash
python evaluate.py
```

## Results

The model is evaluated using:
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- mAP (for YOLOv8)

## Future Improvements
- Increase dataset size
- Improve classification accuracy
- Deploy as a web application
- Real-time detection support
- Mobile application integration

## Contributors

- Shreya Jagadish
- Team Members

## License

This project is for educational and research purposes.
