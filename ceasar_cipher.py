"""
Ceasar Cipher CLI
"""

__author__ = "VFM | SB"
__email__ = "vfm_sb@proton.me"
__copyright__ = "Copyleft 2022"
__license__ = "MIT"
__version__ = "0.2.0"
__maintainer__ = "VFM | SB"
__status__ = "Practice"

from string import ascii_lowercase # Built-in Modules


def cipher_alphabet(shift: int) -> list:
    shifted_alphabet = ["*" for _ in range(len(ascii_lowercase))]
    for i in range(len(ascii_lowercase)):
        shifted_alphabet[i - shift] = ascii_lowercase[i]
    return shifted_alphabet

def encrypt(message: str, shift: int) -> str:
    shifted_alphabet = cipher_alphabet(shift)
    encrypted_message = ""
    for letter in message:
        encrypted_message += shifted_alphabet[ascii_lowercase.index(letter)]
    return encrypted_message

def decrypt(encrypted_message: str, shift: int) -> str:
    shifted_alphabet = cipher_alphabet(shift)
    decrypted_message = ""
    for letter in encrypted_message:
        decrypted_message += ascii_lowercase[shifted_alphabet.index(letter)]
    return decrypted_message


# Function Testing
if __name__ == "__main__":
    pass
    # message = "zulu"
    # shift_amount = 1
    # encrypted_message = encrypt(message, shift_amount)
    # print(encrypted_message)
    # decrypted_message = decrypt(encrypted_message, shift_amount)
    # print(decrypted_message)