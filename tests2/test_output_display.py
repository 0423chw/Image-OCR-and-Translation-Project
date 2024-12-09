import unittest
import os
from text_translation.output_display import overlay_text_on_image

class TestOutputDisplay(unittest.TestCase):
    
    def test_overlay_text_on_image(self):
        text = "안녕하세요, 이것은 테스트입니다."
        image_path = "sample_image.jpg"  # 실제 이미지 경로로 변경
        output_path = "test_output_image.jpg"
        
        overlay_text_on_image(image_path, text, output_path)
        
        # 결과 이미지가 생성되었는지 확인
        self.assertTrue(os.path.exists(output_path))
        
        # 생성된 이미지 파일 삭제 (clean up)
        os.remove(output_path)

if __name__ == "__main__":
    unittest.main()
