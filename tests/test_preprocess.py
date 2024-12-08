import unittest
from preprocess import preprocess_image
import cv2
import os

class TestImagePreprocessing(unittest.TestCase):

    def test_preprocess_image(self):
        processed_image = preprocess_image("sample_image.jpg")
        cv2.imwrite("test_processed_image.jpg", processed_image)
        self.assertTrue(os.path.exists("test_processed_image.jpg"))

if __name__ == "__main__":
    unittest.main()
