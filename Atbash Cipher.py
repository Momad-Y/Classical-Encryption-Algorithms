def atbash_encrypt(plain_text):
    """
    Encrypts the given plain text using the Atbash cipher.

    The Atbash cipher is a substitution cipher where each letter in the plain text is replaced
    with its mirror image in the alphabet. Non-alphabetic characters are left unchanged.

    Args:
    -   plain_text (str): The plain text to be encrypted.

    Returns:
    -   str: The encrypted text.
    """

    encrypted_text = ""  # encrypted text is stored in this variable

    # Loop through each character in the plain text
    for char in plain_text:
        if (
            char.isalpha()
        ):  # isalpha() checks whether the character is an alphabet or not
            ascii_val = ord(
                char.upper()
            )  # ord() returns the ASCII value of the character
            encrypted_text += chr(
                155 - ascii_val
            )  # atbash encryption formula (155 = 65 + 90 = A + Z)
        else:
            encrypted_text += char  # if the character is not an alphabet

    return encrypted_text  # return the encrypted text


def atbash_decrypt(cipher_text):
    """
    Decrypts a given cipher text using the Atbash cipher.

    Parameters:
    -   cipher_text (str): The encrypted text to be decrypted.

    Returns:
    -   str: The decrypted text.
    """

    decrypted_text = ""  # decrypted text is stored in this variable

    # Loop through each character in the encrypted text
    for char in cipher_text:
        if (
            char.isalpha()
        ):  # isalpha() checks whether the character is an alphabet or not
            ascii_val = ord(
                char.upper()
            )  # ord() returns the ASCII value of the character
            decrypted_text += chr(
                155 - ascii_val
            )  # atbash decryption formula is same as encryption formula
        else:
            decrypted_text += char  # if the character is not an alphabet

    return decrypted_text  # return the decrypted text


plain_text_input = input("Enter the text to encrypt: ")  # take the plain text as input

# Encrypt and decrypt the plain text
cipher_text = atbash_encrypt(plain_text_input)
plain_text = atbash_decrypt(cipher_text)

# Print the results
print("Encrypted text:", cipher_text)
print("Decrypted text:", plain_text)
