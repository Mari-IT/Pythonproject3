from googletrans import Translator, LANGUAGES

trans_instance = Translator()


def CodeLang(lang: str) -> str:
    reverse_LANGUAGES = {value.lower(): key for key, value in LANGUAGES.items()}
    lang_identifier_lower = lang.lower()

    if lang_identifier_lower in reverse_LANGUAGES:
        return reverse_LANGUAGES[lang_identifier_lower]

    if lang_identifier_lower in LANGUAGES:
        return LANGUAGES[lang_identifier_lower].capitalize()

    return "Language is not found"


def TransLate(text: str, src: str, dest: str) -> str:
    translation_result = trans_instance.translate(text, src=src, dest=dest)
    if translation_result:
        return translation_result.text
    else:
        return "Translation error"


def LangDetect(text: str, set: str = "all") -> str:
    detection_result = trans_instance.detect(text)

    if set == "lang":
        return detection_result.lang
    elif set == "confidence":
        return str(detection_result.confidence)
    elif set == "all":
        return f"Detected(lang={detection_result.lang}, confidence={detection_result.confidence})"
    else:
        return "Invalid parameter set"


def LanguageList(out: str = "screen", text: str = None) -> str:
    header = "N Language              ISO-639 code Text"
    separator = "-" * 70

    translations = []

    for index, (code, lang) in enumerate(LANGUAGES.items(), 1):
        translated_text = TransLate(text, src='uk', dest=code) if text else ""
        translations.append(f"{index:<2} {lang:<22} {code:<14} {translated_text}")

    output = "\n".join([header, separator] + translations)

    if out == "screen":
        print(output)
        return "Ok"
    elif out == "file":
        with open("language_list_gt.txt", "w", encoding="utf-8") as file:
            file.write(output)
        return "Ok"
    else:
        return "Invalid parameter out"
