import unittest
from text_translation.translate import translate_text

class TestTranslation(unittest.TestCase):
    
    def test_translation(self):
        input_text = "Hello, how are you?"
        translated_text = translate_text(input_text, target_lang="ko")
        self.assertIsInstance(translated_text, str)
        self.assertTrue(len(translated_text) > 0)

    def test_translation_accuracy(self):
        input_text = "Good morning!"
        expected_translation = "좋은 아침!"
        
        translated_text = translate_text(input_text, target_lang="ko")
        
        self.assertEqual(translated_text, expected_translation)

if __name__ == "__main__":
    unittest.main()

