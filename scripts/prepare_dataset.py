import os
import shutil
import random
import xml.etree.ElementTree as ET
from sklearn.model_selection import train_test_split

# ==============================
# Paths
# ==============================
RAW_DIR = "dataset/raw"
OUTPUT_DIR = "dataset"

# ==============================
# Create folders
# ==============================
folders = [
    "train/images",
    "train/labels",
    "valid/images",
    "valid/labels",
    "test/images",
    "test/labels",
]

for folder in folders:
    os.makedirs(os.path.join(OUTPUT_DIR, folder), exist_ok=True)

# ==============================
# Get all images
# ==============================
images = []

for file in os.listdir(RAW_DIR):
    if file.lower().endswith(".jpg"):
        images.append(file)

random.shuffle(images)

train_imgs, temp_imgs = train_test_split(images, test_size=0.30, random_state=42)
valid_imgs, test_imgs = train_test_split(temp_imgs, test_size=0.33, random_state=42)


def convert(image_list, split):

    for img in image_list:

        xml_file = img.replace(".jpg", ".xml")

        image_path = os.path.join(RAW_DIR, img)
        xml_path = os.path.join(RAW_DIR, xml_file)

        shutil.copy(image_path,
                    os.path.join(OUTPUT_DIR, split, "images", img))

        tree = ET.parse(xml_path)
        root = tree.getroot()

        width = int(root.find("size/width").text)
        height = int(root.find("size/height").text)

        txt_name = img.replace(".jpg", ".txt")
        txt_path = os.path.join(OUTPUT_DIR, split, "labels", txt_name)

        with open(txt_path, "w") as f:

            for obj in root.findall("object"):

                cls = 0

                xmin = float(obj.find("bndbox/xmin").text)
                ymin = float(obj.find("bndbox/ymin").text)
                xmax = float(obj.find("bndbox/xmax").text)
                ymax = float(obj.find("bndbox/ymax").text)

                x = ((xmin + xmax) / 2) / width
                y = ((ymin + ymax) / 2) / height
                w = (xmax - xmin) / width
                h = (ymax - ymin) / height

                f.write(f"{cls} {x} {y} {w} {h}\n")


convert(train_imgs, "train")
convert(valid_imgs, "valid")
convert(test_imgs, "test")

print("Dataset Prepared Successfully!")