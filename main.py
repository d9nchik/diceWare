from random import randint
from sys import argv


def read_data(file_name: str) -> dict:
    word_dict = {}
    with open(file_name) as file:
        for line in file:
            words = line.split()
            word_dict[int(words[0])] = words[1]
    if len(word_dict) != 6 ** 5:
        raise Exception('{} is corrupted'.format(file_name))
    return word_dict


def generate_dice_throw() -> int:
    return randint(1, 6)


def generate_word(word_dict: dict) -> str:
    number = 0
    for n in range(5):
        number *= 10
        number += generate_dice_throw()
    return word_dict[number]


def generate_passphrase(word_number: int, word_dict: dict) -> str:
    passphrase = generate_word(word_dict)
    for n in range(word_number - 1):
        passphrase += ' ' + generate_word(word_dict)
    return passphrase


def console_data():
    word_dict = read_data('data.txt')
    word_number = int(input('Enter number of words in your passphrase: '))
    print(generate_passphrase(word_number, word_dict))


def console_arguments():
    word_dict = read_data('data.txt')
    word_number = int(argv[1])
    print(generate_passphrase(word_number, word_dict))


if __name__ == '__main__':
    console_arguments()
