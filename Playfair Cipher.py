def initialize_text(text: str):
    """
    Initializes the plain text for the Playfair Cipher encryption.

    Args:
    -   text (str): The plain text to be encrypted.

    Returns:
    -   list: A list of pairs of two characters representing the initialized plain text.
    """
    text = text.upper()  # converting the plain text to upper case

    # Loop through the plain text and insert a filler character between two consecutive identical characters
    for i in range(len(text)):
        if i % 2 == 0:
            char_1 = text[i]  # stores the first character of the pair
        if i % 2 == 1:
            char_2 = text[i]  # stores the second character of the pair

            # If the two characters are identical, insert a filler character
            if char_1 == char_2:
                text = text[:i] + "X" + text[i:]

    # If the length of the plain text is odd, append a filler character at the endS
    if len(text) % 2 == 1:
        text += "X"

    # Divide the plain text into pairs of two
    plain_text_list = [text[i : i + 2] for i in range(0, len(text), 2)]

    return plain_text_list  # return the initialized plain text


def initialize_playfair_matrix(key_text: str):
    """
    Initializes a Playfair matrix based on a given key text.

    Args:
    -   key_text (str): The key text used to generate the Playfair matrix.

    Returns:
    -   list: A 5x5 matrix representing the Playfair matrix.
    """

    # Initialize an empty matrix of size 5x5
    playfair_matrix = [["" for i in range(5)] for j in range(5)]

    key_text = key_text.upper()  # converting the key to upper case
    aplhabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # J is omitted
    main_string = key_text + aplhabet  # appending the key to the alphabet

    # Remove duplicate characters from the main string
    main_string = "".join(dict.fromkeys(main_string))

    # Loop through each character in the key
    for i in range(5):
        for j in range(5):
            playfair_matrix[i][j] = main_string[i * 5 + j]

    # Loop through the remaining characters of the alphabet

    return playfair_matrix  # return the initialized playfair matrix


def playfair_encrypt(plain_text: str, key_text: str):
    """
    Encrypts the given plain text using the Playfair cipher algorithm.

    Parameters:
    -   plain_text (str): The plain text to be encrypted.
    -   key_text (str): The key text used to initialize the Playfair matrix.

    Returns:
    -   str: The encrypted text.
    """

    initialized_plain_text = initialize_text(plain_text)  # initialize the plain text
    playfair_matrix = initialize_playfair_matrix(
        key_text
    )  # initialize the playfair matrix

    encrypted_text = ""  # encrypted text is stored in this variable
    # Loop through each pair of characters in the initialized plain text
    for pair in initialized_plain_text:
        char_1 = pair[0]  # stores the first character of the pair
        char_2 = pair[1]  # stores the second character of the pair

        # Find the row and column of the two characters in the playfair matrix
        for i in range(5):
            for j in range(5):
                if playfair_matrix[i][j] == char_1:
                    row_1 = i
                    col_1 = j
                if playfair_matrix[i][j] == char_2:
                    row_2 = i
                    col_2 = j

        # If the two characters are in the same row, shift them to the right by 1
        if row_1 == row_2:
            encrypted_char_1 = playfair_matrix[row_1][(col_1 + 1) % 5]
            encrypted_char_2 = playfair_matrix[row_2][(col_2 + 1) % 5]

        # If the two characters are in the same column, shift them down by 1
        elif col_1 == col_2:
            encrypted_char_1 = playfair_matrix[(row_1 + 1) % 5][col_1]
            encrypted_char_2 = playfair_matrix[(row_2 + 1) % 5][col_2]

        # If the two characters are not in the same row or column, swap their columns
        else:
            encrypted_char_1 = playfair_matrix[row_1][col_2]
            encrypted_char_2 = playfair_matrix[row_2][col_1]

        encrypted_text += (
            encrypted_char_1 + encrypted_char_2
        )  # append the encrypted characters to the encrypted text

    return encrypted_text  # return the encrypted text


def playfair_decrypt(cipher_text: str, key_text: str):
    """
    Decrypts a given cipher text using the Playfair cipher algorithm.

    Args:
    -   cipher_text (str): The cipher text to be decrypted.
    -   key_text (str): The key text used for encryption.

    Returns:
    -   str: The decrypted plain text.
    """

    initialized_cipher_text = initialize_text(cipher_text)  # initialize the plain text
    playfair_matrix = initialize_playfair_matrix(
        key_text
    )  # initialize the playfair matrix

    decrypted_text = ""  # decrypted text is stored in this variable
    # Loop through each pair of characters in the initialized plain text
    for pair in initialized_cipher_text:
        char_1 = pair[0]  # stores the first character of the pair
        char_2 = pair[1]  # stores the second character of the pair

        # Find the row and column of the two characters in the playfair matrix
        for i in range(5):
            for j in range(5):
                if playfair_matrix[i][j] == char_1:
                    row_1 = i
                    col_1 = j
                if playfair_matrix[i][j] == char_2:
                    row_2 = i
                    col_2 = j

        # If the two characters are in the same row, shift them to the left by 1
        if row_1 == row_2:
            decrypted_char_1 = playfair_matrix[row_1][(col_1 - 1) % 5]
            decrypted_char_2 = playfair_matrix[row_2][(col_2 - 1) % 5]

        # If the two characters are in the same column, shift them up by 1
        elif col_1 == col_2:
            decrypted_char_1 = playfair_matrix[(row_1 - 1) % 5][col_1]
            decrypted_char_2 = playfair_matrix[(row_2 - 1) % 5][col_2]

        # If the two characters are not in the same row or column, swap their columns
        else:
            decrypted_char_1 = playfair_matrix[row_1][col_2]
            decrypted_char_2 = playfair_matrix[row_2][col_1]

        decrypted_text += (
            decrypted_char_1 + decrypted_char_2
        )  # append the decrypted characters to the decrypted text

    return decrypted_text  # return the decrypted text


# Scan the plain text and key from the user
plain_text = input("Enter the plain text: ")
key_text = input("Enter the key: ")

# Encrypt and decrypt the plain text
cipher_text = playfair_encrypt(plain_text, key_text)
plain_text = playfair_decrypt(cipher_text, key_text)

# Print the cipher text and plain text
print("Cipher text:", cipher_text)
print("Plain text:", plain_text)
