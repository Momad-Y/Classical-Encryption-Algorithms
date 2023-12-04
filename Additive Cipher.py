def additive_encrypt(plain_text: str, key: int):
    """
    Encrypts the given plain text using the additive cipher algorithm.

    Args:
    -   plain_text (str): The plain text to be encrypted.
    -   key (int): The encryption key.

    Returns:
    -   str: The encrypted cipher text.
    """

    cipher_text = ""  # encrypted text is stored in this variable

    # Loop through each character in the plain text
    for char in plain_text:
        if (
            char.isalpha()
        ):  # isalpha() checks whether the character is an alphabet or not
            ascii_val = ord(
                char.upper()
            )  # ord() returns the ASCII value of the character
            shifted_val = (
                ((ascii_val - 65) + key) % 26
            ) + 65  # 65 is the ASCII value of 'A' (additive encryption formula)
            cipher_text += chr(
                shifted_val
            )  # chr() returns the character corresponding to the ASCII value
        else:
            cipher_text += char  # if the character is not an alphabet

    return cipher_text  # return the encrypted text


def additive_decrypt(cipher_text, key):
    """
    Decrypts a given cipher text using the additive cipher algorithm.

    Parameters:
    -   cipher_text (str): The cipher text to be decrypted.
    -   key (int): The key used for decryption.

    Returns:
    -   str: The decrypted plain text.
    """

    return additive_encrypt(cipher_text, -key)  # -key is used to shift backwards


def rot13_encrypt(plain_text):
    """
    Encrypts the given plain text using the ROT13 encryption algorithm.

    Parameters:
    -   plain_text (str): The plain text to be encrypted.

    Returns:
    -   str: The encrypted text.
    """

    return additive_encrypt(plain_text, 13)  # 13 is the key for rot13 encryption


def rot13_decrypt(cipher_text):
    """
    Decrypts the given cipher text using the ROT13 algorithm.

    Parameters:
    -   cipher_text (str): The text to be decrypted.

    Returns:
    -   str: The decrypted text.
    """

    return additive_decrypt(cipher_text, 13)  # -13 is the key for rot13 decryption


plain_text_input = input(
    "Enter the plain text: "
)  # take the plain text as input from the user
key = int(input("Enter the key: "))  # take the key as input from the user

cipher_text = additive_encrypt(
    plain_text_input, key
)  # encrypt the plain text using the additive cipher algorithm
plain_text = additive_decrypt(
    cipher_text, key
)  # decrypt the cipher text using the additive cipher algorithm

cipher_text_rot13 = rot13_encrypt(
    plain_text
)  # encrypt the plain text using the rot13 algorithm
plain_text_rot13 = rot13_decrypt(
    cipher_text_rot13
)  # decrypt the cipher text using the rot13 algorithm

# print the cipher text and plain text for additive cipher
print("Cipher text:", cipher_text)
print("Plain text:", plain_text)

# print the cipher text and plain text for rot13
print("Cipher text (rot13):", cipher_text_rot13)
print("Plain text (rot13):", plain_text_rot13)
