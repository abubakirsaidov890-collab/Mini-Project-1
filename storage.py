
import json
import os

FILE = "budget.json"

def load_data():
    if os.path.exists(FILE):
        try:
            with open(FILE, "r", encoding="utf-8") as file:
                data = json.load(file)

            data.setdefault("income", 0)
            data.setdefault("expenses", 0)
            data.setdefault("categories", {})
            data.setdefault("limit", 0)

            return data

        except (json.JSONDecodeError, OSError):
            print("Не удалось прочитать данные. Создан новый бюджет.")

    return {
        "income": 0,
        "expenses": 0,
        "categories": {},
        "limit": 0
    }

def save_data(data):
    with open(FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

