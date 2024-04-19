import random

def get_numbers_ticket(min, max, quantity):
    if max - min + 1 < quantity:
        return []
    elif min >= 1 and max <= 1000:
        ticket_numbers = random.sample(range(min, max + 1), quantity)
        ticket_numbers.sort()
        return ticket_numbers
    return []

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
