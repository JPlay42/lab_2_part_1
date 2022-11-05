from abc import ABC


class Interface(ABC):
    @staticmethod
    def _input_options(amount: int):
        answer = int(input('Your answer: '))
        if answer < 1 or answer > amount:
            raise ValueError('There is no option with this number')
