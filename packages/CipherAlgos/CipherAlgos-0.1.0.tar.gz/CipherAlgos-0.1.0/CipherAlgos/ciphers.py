def vigenere_cipher(message, key):
    """
    Encrypts a message using the Vigenere cipher.

    Parameters:
    message (str): The message to be encrypted.
    key (str): The keyword, which determines the shift for each character in the message.

    Returns:
    str: The encrypted message.
    """
    encrypted_message = ""
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    message_int = [ord(i) for i in message]
    for i in range(len(message_int)):
        value = (message_int[i] + key_as_int[i % key_length]) % 256
        encrypted_message += chr(value)
    return encrypted_message


def caesar_cipher(message, shift):
    """
    Encrypts a message using the Caesar cipher.

    Parameters:
    message (str): The message to be encrypted.
    shift (int): The number of positions each character in the message will be shifted.

    Returns:
    str: The encrypted message.
    """
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift_amount = shift % 26
            char_code = ord(char) + shift_amount
            if char.islower():
                if char_code > ord('z'):
                    char_code -= 26
                elif char_code < ord('a'):
                    char_code += 26
            elif char.isupper():
                if char_code > ord('Z'):
                    char_code -= 26
                elif char_code < ord('A'):
                    char_code += 26
            encrypted_message += chr(char_code)
        else:
            encrypted_message += char
    return encrypted_message


def xor_cipher(message, key):
    """
    Encrypts a message using the XOR encryption.

    Parameters:
    message (str): The message to be encrypted.
    key (str): The encryption key used for XOR operation.

    Returns:
    str: The encrypted message.
    """
    encrypted_message = ""
    key_length = len(key)
    for i, char in enumerate(message):
        encrypted_message += chr(ord(char) ^ ord(key[i % key_length]))
    return encrypted_message



if __name__ == "__main__":

    message = "example message"
    shift = 3
    key = "key"

    encrypted_caesar = caesar_cipher(message, shift)
    print(f"Caesar Cipher: {encrypted_caesar}")

    encrypted_xor = xor_cipher(message, key)
    print(f"XOR Cipher: {encrypted_xor}")

    encrypted_vigenere = vigenere_cipher(message, key)
    print(f"Vigenere Cipher: {encrypted_vigenere}")
