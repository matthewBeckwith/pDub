import random
from enum import Enum


class Strength(Enum):
    NORMAL = 1
    ADVANCED = 2


letters = [
    'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G',
    'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N',
    'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U',
    'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z'
]

special_characters = [
    '.', '-', '*', '!', '/', '@', '#', '$', '%', '^', '&', '(', ')', '_',
    '[', ']', '{', '}', '|', '<', '>', '?', '`', '~'
]


def generate(length, strength) -> str:
    strength_value = Strength[strength.upper()].value if strength.upper() in Strength.__members__ else Strength.NORMAL
    new_password = []
    for i in range(length):
        if i != 0 and i % 3 == 0 and strength_value == 2:
            new_password.append(random.choice(special_characters))
        else:
            new_password.append(random.choice(letters))
    return ''.join(new_password)
