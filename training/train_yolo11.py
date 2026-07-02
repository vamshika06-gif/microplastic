from ultralytics import YOLO

# Load YOLO11 Nano pretrained model
model = YOLO("yolo11n.pt")

# Train
model.train(
    data="dataset/data.yaml",
    epochs=100,
    imgsz=640,
    batch=8,
    project="runs",
    name="microplastic_yolo11"
)

print("Training Completed Successfully!")