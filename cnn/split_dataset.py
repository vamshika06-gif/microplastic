import os
import shutil
import random

# Source dataset
source_dir = "cnn_dataset"

# Destination folders
train_dir = os.path.join(source_dir, "train")
valid_dir = os.path.join(source_dir, "valid")
test_dir = os.path.join(source_dir, "test")

classes = ["hard", "line", "pellet", "foam"]

for cls in classes:
    images = os.listdir(os.path.join(source_dir, cls))
    random.shuffle(images)

    train_split = int(0.7 * len(images))
    valid_split = int(0.85 * len(images))

    train_imgs = images[:train_split]
    valid_imgs = images[train_split:valid_split]
    test_imgs = images[valid_split:]

    for folder in [train_dir, valid_dir, test_dir]:
        os.makedirs(os.path.join(folder, cls), exist_ok=True)

    for img in train_imgs:
        shutil.copy(
            os.path.join(source_dir, cls, img),
            os.path.join(train_dir, cls, img)
        )

    for img in valid_imgs:
        shutil.copy(
            os.path.join(source_dir, cls, img),
            os.path.join(valid_dir, cls, img)
        )

    for img in test_imgs:
        shutil.copy(
            os.path.join(source_dir, cls, img),
            os.path.join(test_dir, cls, img)
        )

print("Dataset split completed successfully!")