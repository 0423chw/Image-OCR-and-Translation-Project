from transformers import MarianMTModel, MarianTokenizer

def translate_text(text, target_lang="ko"):
    """
    Translate text using Hugging Face's MarianMTModel.
    :param text: The text to be translated.
    :param target_lang: Target language code (default is 'ko' for Korean).
    :return: Translated text.
    """
    model_name = f'Helsinki-NLP/opus-mt-en-{target_lang}'
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)

    # Tokenize input text
    tokens = tokenizer(text, return_tensors="pt", padding=True, truncation=True)

    # Generate translated text
    translated = model.generate(**tokens)

    # Decode and return the translated text
    return tokenizer.decode(translated[0], skip_special_tokens=True)

if __name__ == "__main__":
    # Example text from OCR extraction
    input_text = """
    But the human tongue can lead to far more devastating outcomes, 
    which are not always apparent in the first instance. We may, in some cases, 
    never know who assaulted us, because they act as if they are your best friends. 
    Especially when you perform in a leadership position, you will encounter people 
    who behave very friendly around you and agree with everything you say. However, 
    these same individuals may engage in badmouthing and backstabbing as soon as 
    they are out of sight. It is, therefore, wise to be friendly with everyone and yet 
    practice healthy detachment by refraining from telling people your innermost 
    secrets. By practicing this method, you can avoid making yourself a potential 
    victim of others' jealousy and hatred. The more people know about you, the more 
    vulnerable you become to their negativity.
    """

    translated_text = translate_text(input_text, target_lang="ko")
    print(f"Translated Text:\n{translated_text}")
