import random
from enum import Enum

class Unit(Enum):
    CELSIUS = "C"
    FAHRENHEIT = "F"
    KELVIN = "K"

cities = ["Абакан", "Сорск", "Усть-Абакан", "Таштып", "Боград", "Копьёво", "Абаза", "Черногорск"]
weather_data = {city: round(random.uniform(-30, 40), 1) for city in cities}

def convert_temperature(celsius):
    return [
        f"{celsius}C",
        f"{round(celsius * 9 / 5 + 32, 1)}F",
        f"{round(celsius + 273.15, 1)}K"
    ]

def get_weather(city):
    if city not in weather_data:
        return f"Город {city} не найден."
    return convert_temperature(weather_data[city])

def filter_cities(sign):
    return list(
        filter(
            lambda item: (item[1] >= 0 if sign == "+" else item[1] < 0),
            [(city, temp, Unit.CELSIUS.value) for city, temp in weather_data.items()]
        )
    )

def sort_cities(descending=False):
    return sorted(weather_data.items(), key=lambda x: x[1], reverse=descending)

if __name__ == "__main__":

    print("\nПогода для города Абакан:")
    print(get_weather("Абакан"))

    print("\nГорода с температурой больше или равной 0°C:")
    print(filter_cities("+"))

    order = input("\nВведите 'asc' для сортировки по возрастанию или 'desc' для сортировки по убыванию: ")
    if order == "asc":
        print("Сортировка по возрастанию:", sort_cities())
    elif order == "desc":
        print("Сортировка по убыванию:", sort_cities(descending=True))
    else:
        print("Некорректный ввод!")
