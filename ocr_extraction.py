import pytesseract
from preprocess import preprocess_image

# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    processed_image = preprocess_image(image_path)
    text = pytesseract.image_to_string(processed_image, lang='eng')
    return text

if __name__ == "__main__":
    image_path = r"C:\Users\Owner\Desktop\project\image_processing\sample_image.jpg"
    text = extract_text_from_image(image_path)
    with open(r"C:\Users\Owner\Desktop\project\image_processing\extracted_text.txt", "w") as text_file:
        text_file.write(text)

    print("extracted text\n:", text)
