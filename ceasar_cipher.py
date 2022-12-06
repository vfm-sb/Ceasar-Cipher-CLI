"""
Ceasar Cipher CLI
"""

__author__ = "VFM | SB"
__email__ = "vfm_sb@proton.me"
__copyright__ = "Copyleft 2022"
__license__ = "MIT"
__version__ = "0.6.0"
__maintainer__ = "VFM | SB"
__status__ = "Practice"

import os
from string import ascii_lowercase # Built-in Modules


AVAILABLE_OPERATIONS = ["encode", "decode"]


def cipher_alphabet(shift: int) -> list:
    alphabet_length = len(ascii_lowercase)
    shift = shift % alphabet_length
    shifted_alphabet = ["*" for _ in range(alphabet_length)]
    for i in range(alphabet_length):
        shifted_alphabet[i - shift] = ascii_lowercase[i]
    return shifted_alphabet

def cipher(start_text: str, shift: int, operation: str) -> str:
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


# Function Testing
if __name__ == "__main__":
    pass
    # message = "zulu"
    # shift_amount = 1
    # encrypted_message = encrypt(message, shift_amount)
    # print(encrypted_message)
    # decrypted_message = decrypt(encrypted_message, shift_amount)
    # print(decrypted_message)