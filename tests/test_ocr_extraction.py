import unittest
from ocr_extraction import extract_text_from_image

class TestOCRExtraction(unittest.TestCase):

    def test_extract_text(self):
        text = extract_text_from_image("sample_image.jpg")
        self.assertIsInstance(text, str)
        self.assertTrue(len(text) > 0)

if __name__ == "__main__":
    unittest.main()
