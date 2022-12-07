"""A Simple Ceasar Cipher Program for CLI"""

__author__ = "VFM | SB"
__email__ = "vfm_sb@proton.me"
__copyright__ = "Copyleft 2022"
__license__ = "MIT"
__version__ = "0.6.2"
__maintainer__ = "VFM | SB"
__status__ = "Practice"

import os
from string import ascii_lowercase # Built-in Modules


AVAILABLE_OPERATIONS = ["encode", "decode"]


def cipher_alphabet(shift: int) -> list:
    """Shifts The Alphabet Based on the Given Shift Number
    Argument:
        shift (int): Shift Amount
    Returns:
        list: Shifted Alphabet for Ceasar Cipher
    """
    alphabet_length = len(ascii_lowercase)
    shift = shift % alphabet_length
    shifted_alphabet = ["*" for _ in range(alphabet_length)]
    for i in range(alphabet_length):
        shifted_alphabet[i - shift] = ascii_lowercase[i]
    return shifted_alphabet

def cipher(start_text: str, shift: int, operation: str) -> str:
    """It Encodes or Decodes Given Text, Based on Operation Type
    Arguments:
        start_text (str): Text to be Encrypted or Decrypted
        shift (int): Shift Amount for cipher_alphabet()
        operation (str): Operation Type ("encode" | "decode")
    Returns:
        end_text (str): Encrypted or Decrypted Text
    """
    shifted_alphabet = cipher_alphabet(shift)
    end_text = ""
    for char in start_text.lower():
        if char not in ascii_lowercase:
            end_text += char
            continue
        if operation == "encode":
            shifted_char = shifted_alphabet[ascii_lowercase.index(char)]
        else:
            shifted_char = ascii_lowercase[shifted_alphabet.index(char)]
        end_text += shifted_char
    return end_text


def main():
    """Executive Main Function"""
    os.system("clear")
    print(f"Ceasar Cipher CLI v{__version__}")
    print("-.-. . .- ... .- .-.    -.-. .. .--. .... . .-.\n")
    is_end = False
    while not is_end:
        operation = input(
            'Choose an Operation '
            '("encode" to Encrypt, "decode" to Decrypt):\n'
        )
        if operation not in AVAILABLE_OPERATIONS:
            print("Invalid Operation Command!", "Try Again.\n", sep="\n")
            continue
        text = input(f"Message to {operation.capitalize()}:\n")
        shift_amount = int(input("Shift Number:\n"))
        print(
            f"{operation.capitalize()}d Message:\n",
            cipher(text, shift_amount, operation),
            sep=""
        )
        print('\nWould You Like to Continue? ("yes" | "no")')
        restart = input()
        if restart == "no" or restart != "yes":
            is_end = True
            print("Good Bye!")
        else:
            print()


main()
