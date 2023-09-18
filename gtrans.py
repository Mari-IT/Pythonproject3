from translation_package import module1gt
from translation_package.module1gt import LangDetect, TransLate, CodeLang, LanguageList
if __name__ == "__main__":

    print("1. Identifying of text language:")
    text = "Hello, world!"
    print(f"Text: {text}")
    print(LangDetect(text))

    print("\n2. Translation:")
    dest_lang = "uk"
    print(f"Text to be translated into {dest_lang}: {TransLate(text, src='auto', dest=dest_lang)}")

    print("\n3. Identifying of the language code:")
    lang_name = "Ukrainian"
    print(f"Language code for {lang_name}: {CodeLang(lang_name)}")

    print("\n4. Output of the languages table:")
    language_list_result = LanguageList(out="screen", text="Good afternoon")
    print(language_list_result)
