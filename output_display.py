from PIL import Image, ImageDraw, ImageFont

def overlay_text_on_image(image_path, text, output_path="output_image.jpg"):
    """
    Overlay translated text on an image.
    :param image_path: Path to the input image.
    :param text: Translated text to overlay on the image.
    :param output_path: Path to save the output image.
    """
    # Open the image
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    # Load a font
    font = ImageFont.load_default()

    # Define the position and overlay the text
    text_position = (50, 50)
    draw.text(text_position, text, font=font, fill="black")

    # Save the output image
    image.save(output_path)
    print(f"Output image saved to {output_path}")

if __name__ == "__main__":
    # Example usage
    example_image = "sample_image.jpg"
    translated_text = """
    하지만 인간의 혀는 훨씬 더 파괴적인 결과를 초래할 수 있습니다. 
    처음에는 항상 명백하지 않을 수 있습니다. 우리는 어떤 경우에는 
    우리를 공격한 사람이 누구인지 모를 수도 있습니다, 왜냐하면 그들이 
    마치 가장 친한 친구인 것처럼 행동하기 때문입니다. 특히 리더십 위치에서 
    활동할 때, 당신은 매우 친절하게 행동하며 당신이 말하는 모든 것에 동의하는 사람들을 만날 것입니다. 
    그러나 이러한 사람들은 당신이 보지 않을 때 나쁜 말과 배신을 할 수 있습니다. 
    따라서 모든 사람에게 친절하게 대하면서도, 자신의 내밀한 비밀을 말하지 않는 건강한 
    거리를 두는 연습을 하는 것이 현명합니다. 이 방법을 실천하면 다른 사람들의 질투와 증오의 
    잠재적인 피해자가 되는 것을 피할 수 있습니다. 사람들이 당신에 대해 알수록, 그들의 부정적인 
    에너지에 더 취약해집니다.
    """
    overlay_text_on_image(example_image, translated_text, output_path="translated_output.jpg")
