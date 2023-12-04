def vigenere_encrypt(plain_text, key_text):
    """
    Encrypts the given plain text using the Vigenere cipher algorithm.

    Args:
    -   plain_text (str): The plain text to be encrypted.
    -   key_text (str): The key text used for encryption.

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

            key = (
                ord(key_text[0].upper()) - 65
            )  # getting the key value for the current character

            encrypted_char = chr(
                (((ascii_val - 65) + key) % 26) + 65
            )  # 65 is the ASCII value of 'A' (vigenere encryption formula)

            # rotating the key text
            key_text = key_text + key_text[0]
            key_text = key_text[1:]

            encrypted_text += encrypted_char  # chr() returns the character corresponding to the ASCII value
        else:
            encrypted_text += char  # if the character is not an alphabet

        # if the length of the encrypted text is equal to the length of the plain text, break the loop
        if len(encrypted_text) == len(plain_text):
            break

    return encrypted_text  # return the encrypted text


def vigenere_decrypt(cipher_text, key_text):
    """
    Decrypts the given Vigenere cipher text using the provided key.

    Args:
    -   cipher_text (str): The encrypted text to be decrypted.
    -   key_text (str): The key used for decryption.

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
            key = (
                ord(key_text[0].upper()) - 65
            )  # getting the key value for the current character
            decrypted_char = chr(
                ((ascii_val - 65) - key) % 26 + 65
            )  # vigenere decryption formula

            # rotating the key text
            key_text = key_text + key_text[0]
            key_text = key_text[1:]
            decrypted_text += decrypted_char
        else:
            decrypted_text += char  # if the character is not an alphabet

        # if the length of the decrypted text is equal to the length of the encrypted text, break the loop
        if len(decrypted_text) == len(cipher_text):
            break

    return decrypted_text  # return the decrypted text


# Take the plain text and key as input
plain_text_input = input("Enter the plain text: ")
key = input("Enter the key: ")


# Encrypt and decrypt the plain text
cipher_text = vigenere_encrypt(plain_text_input, key)
plain_text = vigenere_decrypt(cipher_text, key)

# Print the results
print("Encrypted text:", cipher_text)
print("Decrypted text:", plain_text)
