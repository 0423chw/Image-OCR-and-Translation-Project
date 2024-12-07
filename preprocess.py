import cv2
import numpy as np

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    _, binary_image = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return binary_image

if __name__ == "__main__":
    processed_image = preprocess_image("sample_image.jpg")
    cv2.imwrite("processed_image.jpg", processed_image)
