import random
from words import words


def get_a_valid_word(words):
    word = random.choice(words)
    while "_" in word or " " in word:
        word = random.choice(words)

    return word.upper()
