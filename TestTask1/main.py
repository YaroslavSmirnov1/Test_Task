import random


class MarkoPolo:
    @staticmethod
    def check_n_print():
        text = ""
        rand_number = random.randint(0, 1000)
        if rand_number % 3 == 0 and rand_number % 5 == 0 and rand_number != 0:
            text = f'МаркоПоло'
        elif rand_number % 3 == 0 and rand_number != 0:
            text = f'Марко'
        elif rand_number % 5 == 0 and rand_number != 0:
            text = f'Поло'
        return text


m = MarkoPolo()
print(m.check_n_print())
