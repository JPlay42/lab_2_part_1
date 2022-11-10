from abc import ABC, abstractmethod


class Pizza(ABC):
    __all_ingredients = [
        'tomatoes',
        'olives',
        'chicken',
        'salami',
        'tuna',
        'parmesan',
        'mushrooms',
        'tomato sauce',
        'mozzarella',
        'pineapple',
        'paprika',
        'ham',
        'bacon',
        'sausages',
        'oregano',
        'fries sauce',
        'fried potato',
        'bbq sauce'
    ]

    def __init__(self):
        self.__additives = list()

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def content(self):
        pass

    @property
    def available_additives(self):
        additional = list()
        for ingredient in self.__all_ingredients:
            if ingredient not in self.content():
                additional.append(ingredient)

        return additional

    def __str__(self):
        content_string = ', '.join(self.content())
        result = f'{self.name()} ({content_string})'
        if len(self.additives) != 0:
            result += ' + ' + ', '.join(self.additives)
        return result

    @property
    def additives(self):
        return self.__additives

    def filter_and_add(self, additives: list):
        if not isinstance(additives, list):
            raise TypeError('additives is not a list')
        if not all(isinstance(entry, str) for entry in additives):
            raise TypeError('additives list have non-str objects')

        denied = list()
        for entry in additives:
            if entry not in self.available_additives:
                denied.append(entry)
                additives.remove(entry)

        self.__additives = additives
        return denied


class Salami(Pizza):
    def name(self):
        return 'Salami'

    def content(self):
        return [
            'tomato sauce',
            'mozzarella',
            'salami'
        ]


class Hawaii(Pizza):
    def name(self):
        return 'Hawaii'

    def content(self):
        return [
            'tomato sauce',
            'mozzarella',
            'chicken',
            'pineapple',
            'paprika'
        ]


class Calzone(Pizza):
    def name(self):
        return 'Calzone'

    def content(self):
        return [
            'tomato sauce',
            'mozzarella',
            'ham',
            'mushrooms',
            'tomatoes',
            'parmesan'
        ]


class FourMeats(Pizza):
    def name(self):
        return 'Four meats'

    def content(self):
        return [
            'tomato sauce',
            'mozzarella',
            'bacon',
            'ham',
            'salami',
            'sausages'
        ]


class Americano(Pizza):
    def name(self):
        return 'Americano'

    def content(self):
        return [
            'tomato sauce',
            'mozzarella',
            'bacon',
            'salami',
            'ham',
            'olives',
            'paprika',
            'oregano'
        ]


class FriedPizza(Pizza):
    def name(self):
        return 'Fried pizza'

    def content(self):
        return [
            'tomato sauce',
            'fries sauce',
            'sausages',
            'fried potato'
        ]


class Mexican(Pizza):
    def name(self):
        return 'Mexican'

    def content(self):
        return [
            'bbq sauce',
            'mozzarella',
            'bacon',
            'chicken',
            'sausages',
            'tomato'
        ]
