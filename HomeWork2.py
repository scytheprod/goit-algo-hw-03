import random


def get_numbers_ticket(min, max, quantity):
    try:
        numbers = list(range(min, max))
        if max <= 1000 and min >=1:
            random_numbers = random.sample(numbers, quantity)

            return sorted(random_numbers)
        else:
            return list()
    except ValueError:
        return list()
    except TypeError:
        return list()

get_numbers_ticket(1,11,1)