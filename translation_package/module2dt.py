from deep_translator import GoogleTranslator
from langdetect import detect, detect_langs


def CodeLang(lang: str) -> str:
    try:
        detected_lang = detect(lang)
        return detected_lang
    except:
        return "Language is not found"


def TransLate(text: str, src: str, dest: str = 'en') -> str:
    try:
        return GoogleTranslator(source=src, target=dest).translate(text)
    except Exception as e:
        return str(e)


def LangDetect(text: str, set: str = "all") -> str:
    detected_langs = detect_langs(text)
    primary_detection = detected_langs[0]
    detected_lang = primary_detection.lang
    confidence = primary_detection.prob

    if set == "lang":
        return detected_lang
    elif set == "confidence":
        return str(confidence)
    elif set == "all":
        return f"Detected(lang={detected_lang}, confidence={confidence})"
    else:
        return "Invalid parameter set"

def LanguageList(out: str = "screen", text: str = None) -> str:
    header = "N Language              ISO-639 code Text"
    separator = "-" * 70
    translator = GoogleTranslator(source='auto', target='en')
    supported = translator.get_supported_languages(as_dict=True)

    translations = []

    for index, (code, lang) in enumerate(supported.items(), 1):
        translated_text = TransLate(text, src='uk', dest=code) if text else ""
        formatted_index = f"{index:<2}"  # Вирівнюємо номер запису
        formatted_lang = f"{lang:<12}"  # Вирівнюємо мову (збільшено відступ)
        formatted_code = f"{code:<30}"  # Вирівнюємо код
        formatted_text = translated_text.ljust(50)  # Вирівнюємо третій стовпчик до ширини 40 символів
        formatted_row = f"{formatted_index} {formatted_lang} {formatted_code} {formatted_text}"
        translations.append(formatted_row)

    output = "\n".join([header, separator] + translations)

    if out == "screen":
        print(output)
        return "Ok"
    elif out == "file":
        with open("language_list.txt", "w", encoding="utf-8") as file:
            file.write(output)
        return "Ok"
    else:
        return "Invalid parameter out"
