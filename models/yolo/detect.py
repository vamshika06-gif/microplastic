from ultralytics import YOLO
import cv2

# Load trained model
def load_yolo_model(model_path="models/yolo/best.pt"):
    model = YOLO(model_path)
    return model


# Run detection
def run_detection(image, model):
    results = model.predict(image, conf=0.25, verbose=False)
    return results


# Draw bounding boxes
def draw_boxes(image, results):
    annotated = results[0].plot()
    return annotated