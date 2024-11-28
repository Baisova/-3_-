from enum import Enum

class Pizza: # класс пиццы
    def __init__(self):
        self.name = None # название пиццы
        self.dough = None # тесто
        self.sauce = None # соус
        self.cheese = None # сыр
        self.toppings = [] # добавки

    # метод для строкового представления объекта
    def __str__(self):
        return f"Пицца {self.name}: (тесто={self.dough.value}, соус={self.sauce.value}, сыр={self.cheese.value}, добавки={', '.join([t.value for t in self.toppings])})"

class Dough(Enum): # перечисление видов теста
    THIN = "тонкое"
    THICK = "толстое"
    STUFFED = "с начинкой" # новое тесто

class Sauce(Enum): # перечисление видов соуса
    TOMATO = "томатный"
    CREAM = "сливочный"
    PESTO = "песто" # новый соус

class Cheese(Enum): # перечисление видов сыра
    MOZZARELLA = "моцарелла"
    PARMESAN = "пармезан"
    CHEDDAR = "чеддер" # новый сыр

class Topping(Enum): # перечисление видов добавок
    MUSHROOMS = "грибы"
    PEPPERONI = "пепперони" # новая добавка
    OLIVES = "оливки" # новая добавка
    BACON = "бекон" # новая добавка

class PizzaBuilder: # класс постройщика пицц
    def __init__(self):
        self.pizza = Pizza() # инициализация пиццы (объект pizza создается здесь)

    def set_name(self, name): # установить название пиццы
        self.pizza.name = name
        return self # возвращаем объект PizzaBuilder для цепочки вызовов

    def build_dough(self, dough): # выбрать тесто для пиццы
        self.pizza.dough = dough
        return self

    def build_sauce(self, sauce): # выбрать соус
        self.pizza.sauce = sauce
        return self

    def build_cheese(self, cheese): # выбрать сыр
        self.pizza.cheese = cheese
        return self

    def build_toppings(self, toppings): # прибавить добавки
        self.pizza.toppings.extend(toppings)
        return self

    def bake(self): # запечь пиццу (вернуть объект пиццы)
        return self.pizza

# создание настройщика пицц
builder = PizzaBuilder()

# запекаем пиццу
pizza = (builder.set_name("Беконная пицца")
         .build_sauce(Sauce.PESTO)
         .build_cheese(Cheese.CHEDDAR)
         .build_dough(Dough.THICK)
         .build_toppings([Topping.BACON, Topping.PEPPERONI, Topping.OLIVES])
         .bake()
)

print(pizza)

