from datetime import datetime

from task2.src.pizza import Americano, FriedPizza, Mexican, Salami, Hawaii, Calzone, FourMeats


class PizzaOfTheDay:
    __pizzas = [
        Americano,
        FriedPizza,
        Mexican,
        Salami,
        Hawaii,
        Calzone,
        FourMeats
    ]

    def get(self, date: datetime):
        # construct an object with stored class
        return self.__pizzas[date.weekday()]()
