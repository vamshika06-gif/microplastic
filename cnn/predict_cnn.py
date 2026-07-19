import torch
from torchvision import transforms
from PIL import Image
from cnn_model import MicroplasticCNN

# Class names (same order as your cnn_dataset folders)
classes = ["foam", "hard", "line", "pellet"]

# Device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load model
model = MicroplasticCNN(num_classes=4)
model.load_state_dict(torch.load("microplastic_cnn.pth", map_location=device))
model.to(device)
model.eval()

# Image transform
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

def predict_image(image_path):
    image = Image.open(image_path).convert("RGB")
    image = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        output = model(image)
        _, predicted = torch.max(output, 1)

    return classes[predicted.item()]

# Example
if __name__ == "__main__":
    image_path = "sample.jpg"   # Replace with your image
    prediction = predict_image(image_path)
    print("Predicted Class:", prediction)