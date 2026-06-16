import cv2
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

image_path = os.path.join(
    current_dir,
    "..",
    "images",
    "test.jpg"
)

image = cv2.imread(image_path)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 100, 200)

contours, hierarchy = cv2.findContours(
    edges,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

important_contours = []

for contour in contours:
    area = cv2.contourArea(contour)

    if area > 20:
        important_contours.append(contour)

print("Important contours:", len(important_contours))

output = image.copy()

cv2.drawContours(
    output,
    important_contours,
    -1,
    (0, 255, 0),
    2
)

output_path = os.path.join(
    current_dir,
    "..",
    "outputs",
    "important_contours.jpg"
)

cv2.imwrite(output_path, output)

print("Saved!")