from ultralytics import YOLO

# Load trained model
model = YOLO("runs/detect/runs/microplastic_yolo11-2/weights/best.pt")

# Predict on test images
model.predict(
    source="dataset/test/images",
    save=True,
    conf=0.25
)

print("Prediction completed!")