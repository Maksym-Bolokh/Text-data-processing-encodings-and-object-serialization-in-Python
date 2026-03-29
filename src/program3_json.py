import os
from utils.json_handler import write_json, read_json


def main():
    
    people = {
        "Іваненко": ["Іван", "Іванович", 2000],
        "Петренко": ["Петро", "Петрович", 1999],
        "Сидоренко": ["Олена", "Іванівна", 2001],
        "Коваль": ["Марія", "Степанівна", 1998],
        "Мельник": ["Андрій", "Олегович", 2002],
        "Шевченко": ["Тарас", "Григорович", 1997],
        "Бондаренко": ["Оксана", "Миколаївна", 2000],
        "Ткаченко": ["Юрій", "Васильович", 1996],
        "Кравченко": ["Наталія", "Петрівна", 2003],
        "Олійник": ["Віктор", "Сергійович", 1995]
    }

    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(BASE_DIR, '..', 'data', 'people.json')

    
    write_json(people, file_path)
    print("✔ Дані записано у JSON")

    
    data = read_json(file_path)

    print("\n=== ДАНІ З ФАЙЛУ ===")
    for surname, info in data.items():
        print(f"{surname}: {info[0]} {info[1]}, {info[2]}")


if __name__ == "__main__":
    main()