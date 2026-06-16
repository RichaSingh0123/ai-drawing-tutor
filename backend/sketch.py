import cv2
import os

# Get absolute path to image
current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "..", "images", "test.jpg")

print("Loading image from:")
print(image_path)

image = cv2.imread(image_path)

if image is None:
    print("ERROR: Image could not be loaded.")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 100, 200)

output_path = os.path.join(current_dir, "..", "outputs", "sketch.jpg")

cv2.imwrite(output_path, edges)

print("Sketch created successfully!")
print("Saved to:", output_path)