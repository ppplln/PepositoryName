# TODO решите задачу
import json

def task() -> float:
        with open("input.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        summ = 0.0
        for item in data:
            summ += item["score"] * item["weight"]

        return round(summ, 3)

print(task())
