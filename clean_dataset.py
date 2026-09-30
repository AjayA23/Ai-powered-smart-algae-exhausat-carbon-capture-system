from PIL import Image
import os

# Dataset Path
dataset_path = "algae_ai/dataset"

# Image Size
SIZE = (224, 224)

valid_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".webp")

total = 0
cleaned = 0
deleted = 0

for category in os.listdir(dataset_path):

    category_path = os.path.join(dataset_path, category)

    if not os.path.isdir(category_path):
        continue

    print(f"\nChecking Folder: {category}")

    for filename in os.listdir(category_path):

        file_path = os.path.join(category_path, filename)

        # Skip non-image files
        if not filename.lower().endswith(valid_extensions):
            print(f"Skipped: {filename}")
            continue

        total += 1

        try:
            # Open Image
            img = Image.open(file_path)

            # Convert RGB
            img = img.convert("RGB")

            # Resize
            img = img.resize(SIZE)

            # Save
            img.save(file_path)

            cleaned += 1

        except Exception as e:
            print(f"Deleted Corrupted Image: {filename}")
            os.remove(file_path)
            deleted += 1

print("\n==============================")
print("Dataset Cleaning Completed")
print("==============================")
print(f"Total Images Checked : {total}")
print(f"Images Cleaned       : {cleaned}")
print(f"Corrupted Deleted    : {deleted}")