"""
Ceasar Cipher CLI
"""

__author__ = "VFM | SB"
__email__ = "vfm_sb@proton.me"
__copyright__ = "Copyleft 2022"
__license__ = "MIT"
__version__ = "0.5.1"
__maintainer__ = "VFM | SB"
__status__ = "Practice"

from string import ascii_lowercase # Built-in Modules


def cipher_alphabet(shift: int) -> list:
    shift = shift % len(ascii_lowercase)
    shifted_alphabet = ["*" for _ in range(len(ascii_lowercase))]
    for i in range(len(ascii_lowercase)):
        shifted_alphabet[i - shift] = ascii_lowercase[i]
    return shifted_alphabet

def encrypt(message: str, shift: int) -> str:
    shifted_alphabet = cipher_alphabet(shift)
    encrypted_message = ""
    for char in message.lower():
        if char not in ascii_lowercase:
            encrypted_message += char
            continue
        encrypted_message += shifted_alphabet[ascii_lowercase.index(char)]
    return encrypted_message

def decrypt(encrypted_message: str, shift: int) -> str:
    shifted_alphabet = cipher_alphabet(shift)
    decrypted_message = ""
    for char in encrypted_message.lower():
        if char not in ascii_lowercase:
            decrypted_message += char
            continue
        decrypted_message += ascii_lowercase[shifted_alphabet.index(char)]
    return decrypted_message

def main():
    print(f"Ceasar Cipher CLI v{__version__}")
    print("-.-. . .- ... .- .-.    -.-. .. .--. .... . .-.\n")
    is_end = False
    while not is_end:
        operation = input('Choose an Operation ("encode" to Encrypt, "decode" to Decrypt):\n')
        text = input(f"Message to {operation.capitalize()}:\n")
        shift_amount = int(input("Shift Number:\n"))
        if operation == "encode":
            encrypted_message = encrypt(message=text, shift=shift_amount)
            print("Encrypted Message:", encrypted_message)
        elif operation == "decode":
            decrypted_message = decrypt(encrypted_message=text, shift=shift_amount)
            print("Decrypted Message:", decrypted_message)
        else:
            print("Invalid Operation!")
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