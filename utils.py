import random

WORDS = ["alpha", "bravo", "charlie", "delta"]

def get_random_word() -> str:
    """ Возвравщает случайно слово"""
    return random.choice(WORDS)

