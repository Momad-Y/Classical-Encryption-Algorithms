def affine_encrypt(plain_text: str, key: int):
    """
    Encrypts the given plain text using the Affine Cipher algorithm.

    Args:
    -   plain_text (str): The text to be encrypted.
    -   key (int): The encryption key consisting of two integers (a, b).

    Returns:
    -   str: The encrypted text.
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

            encrypted_char = chr(
                ((key[0] * (ascii_val - 65) + key[1]) % 26) + 65
            )  # 65 is the ASCII value of 'A' (affine encryption formula)

            cipher_text += encrypted_char  # chr() returns the character corresponding to the ASCII value
        else:
            cipher_text += char  # if the character is not an alphabet

    return cipher_text  # return the encrypted text


def affine_decrypt(cipher_text, key):
    """
    Decrypts the given cipher text using the Affine Cipher algorithm.

    Parameters:
    -   cipher_text (str): The encrypted text to be decrypted.
    -   key (tuple): The key used for decryption, consisting of two integers (a, b).

    Returns:
    -   plain_text (str): The decrypted text.

    Raises:
    -   ValueError: If the modular inverse of the key does not exist.
    """

    plain_text = ""  # decrypted text is stored in this variable

    # Loop through each character in the encrypted text
    for char in cipher_text:
        if (
            char.isalpha()
        ):  # isalpha() checks whether the character is an alphabet or not
            ascii_val = ord(
                char.upper()
            )  # ord() returns the ASCII value of the character

            m_dash = mod_inverse(key[0], 26)

            if m_dash == -1:
                raise ValueError(
                    "The modular inverse of {} does not exist.".format(key[0])
                )

            decrypted_char = chr(
                ((((ascii_val - 65) - key[1]) * m_dash) % 26) + 65
            )  # 65 is the ASCII value of 'A' (affine decryption formula)

            plain_text += decrypted_char  # chr() returns the character corresponding to the ASCII value
        else:
            plain_text += char  # if the character is not an alphabet

    return plain_text  # return the decrypted text


def mod_inverse(m, n):
    """
    Calculates the modular inverse of a number 'n' with respect to a modulus 'm', if it exists.
    GCD(m, n) must be equal to 1 for the modular inverse to exist.

    Parameters:
    -   m (int): The modulus.
    -   n (int): The number for which the modular inverse is to be calculated.

    Returns:
    -   int: The modular inverse of 'n' with respect to 'm'. Returns -1 if the modular inverse does not exist.
    """

    # Loop through all the numbers from 1 to n
    for i in range(1, n):
        # If the modular inverse exists, return it
        if (m * i) % n == 1:
            return i

    return -1  # Return -1 if the modular inverse does not exist


def multiplicative_encrypt(plain_text, key):
    """
    Encrypts the given plain text using the multiplicative cipher algorithm.

    Parameters:
    -   plain_text (str): The plain text to be encrypted.
    -   key (int): The key used for encryption.

    Returns:
    -   str: The encrypted text.
    """

    return affine_encrypt(
        plain_text, (key, 0)
    )  # 0 is the value of k in multiplicative cipher


def multiplicative_decrypt(cipher_text, key):
    """
    Decrypts a given cipher text using the multiplicative cipher algorithm.

    Parameters:
    -   cipher_text (str): The cipher text to be decrypted.
    -   key (int): The key used for decryption.

    Returns:
    -   str: The decrypted plain text.
    """

    return affine_decrypt(
        cipher_text, (key, 0)
    )  # 0 is the value of k in multiplicative cipher


plain_text_input = input(
    "Enter the plain text: "
)  # take the plain text as input from the user
m = int(input("Enter the multiplicative key: "))  # take the m as input from the user
k = int(input("Enter the additive key: "))  # take the k as input from the user

# key is a tuple consisting of m and k (m is the multiplicative key and k is the additive key)
key = (m, k)

cipher_text = affine_encrypt(
    plain_text_input, key
)  # encrypt the plain text using the affine cipher algorithm
plain_text = affine_decrypt(
    cipher_text, key
)  # decrypt the cipher text using the affine cipher algorithm

cipher_text_multiplicative = multiplicative_encrypt(
    plain_text, m
)  # encrypt the plain text using the multiplicative cipher algorithm
plain_text_multiplicative = multiplicative_decrypt(
    cipher_text_multiplicative, m
)  # decrypt the cipher text using the multiplicative cipher algorithm

# print the cipher text and plain text for affine cipher
print("Encrypted text:", cipher_text)
print("Decrypted text:", plain_text)

# print the cipher text and plain text for multiplicative cipher
print("Encrypted text (multiplicative):", cipher_text_multiplicative)
print("Decrypted text (multiplicative):", plain_text_multiplicative)
