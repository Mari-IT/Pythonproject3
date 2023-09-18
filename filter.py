import json
import re
from translation_package.module2dt import TransLate


def read_config(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def analyze_text(file_path, config):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

        characters_count = len(text)
        words_count = len(text.split())
        sentences_count = len(re.split(r'[.!?]', text))

        if characters_count > config["min_characters"]:
            text = text[:config["min_characters"]]

        if words_count > config["min_words"]:
            words = text.split()
            text = " ".join(words[:config["min_words"]])

        if sentences_count > config["min_sentences"]:
            sentences = re.split(r'[.!?]', text)
            text = " ".join(sentences[:config["min_sentences"]])

        return text, characters_count, words_count, sentences_count


def main():
    config = read_config('config.json')
    text, characters, words, sentences = analyze_text(config["text_file"], config)

    print(f"File Name: {config['text_file']}")
    print(f"File Size: {characters} characters, {words} words, {sentences} sentences")
    translated_text = TransLate(text, src='auto', dest=config["target_language"])

    if config["output"] == "screen":
        print(translated_text)
    else:
        output_file_name = config["text_file"].split('.')[0] + '_' + config["target_language"] + '.txt'
        with open(output_file_name, 'w', encoding='utf-8') as file:
            file.write(translated_text)
        print("Ok")


if __name__ == "__main__":
    main()