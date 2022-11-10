import re
from datetime import datetime

from task2.src.pizza_of_the_day import PizzaOfTheDay

if __name__ == '__main__':
    pizza_of_the_day = PizzaOfTheDay()
    pizza = pizza_of_the_day.get(datetime.now())
    print(f'Today the pizza of the day is {pizza}')
    print('Additional ingredients:')
    for entry in pizza.available_additives:
        print(entry)

    print('Enter additional ingredients you chose (comma-separated)')
    answer = input('Your choice: ')
    additives = list(filter(None, re.split(r',[\s+]?', answer)))
    denied = pizza.filter_and_add(additives)
    if len(denied) != 0:
        denied_string = ', '.join(denied)
        print(f'Ingredients that have not been added: {denied_string}')

    print(f'The ordered pizza is: {pizza}')
