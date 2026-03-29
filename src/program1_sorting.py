from utils.sorter import sort_words


def read_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


import os
from utils.sorter import sort_words


def read_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


def main():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(BASE_DIR, '..', 'data', 'input.txt')

    print("Шлях:", file_path)

    text = read_text(file_path)
    print("=== ОРИГІНАЛЬНИЙ ТЕКСТ ===")
    print(text)

    words = text.replace('\n', ' ').split()
    sorted_words = sort_words(words)

    print("\n=== ВІДСОРТОВАНІ СЛОВА ===")
    print(sorted_words)


if __name__ == "__main__":
    main()