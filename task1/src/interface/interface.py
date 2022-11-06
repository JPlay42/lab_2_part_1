from abc import ABC, abstractmethod


class Interface(ABC):
    def execute(self):
        while True:
            self.run()
            if input('Would you like to continue? (yes/no): ')[0].casefold() == 'y':
                return

    @abstractmethod
    def run(self):
        pass

    @staticmethod
    def _input_options(amount: int):
        answer = int(input('Your answer: '))
        if answer < 1 or answer > amount:
            raise ValueError('There is no option with this number')
