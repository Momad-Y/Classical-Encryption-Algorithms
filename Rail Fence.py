def rail_encrypt(plain_text: str, depth: int):
    """
    Encrypts the given plain text using the Rail Fence cipher algorithm.

    Parameters:
    -   plain_text (str): The plain text to be encrypted.
    -   depth (int): The depth used for encryption.

    Returns:
    -   str: The encrypted text.
    """

    encrypted_text_list = []  # encrypted text is stored in this variable

    plain_text = plain_text.replace(
        " ", ""
    ).upper()  # remove all spaces from the plain text and convert it to uppercase

    plain_text_length = len(plain_text)  # length of the plain text

    # If the length of the plain text is less than the depth, return the plain text
    if plain_text_length < depth:
        return plain_text

    # Loop through each row of the rail fence cipher
    for i in range(depth):
        # Loop through each character in the plain text
        for j in range(i, plain_text_length, depth):
            encrypted_text_list.append(
                plain_text[j]
            )  # append the character to the encrypted text

    return "".join(encrypted_text_list)  # return the encrypted text


def rail_decrypt(cipher_text: str, depth: int):
    """
    Decrypts the given Rail Fence cipher text using the provided depth.

    Parameters:
    -   cipher_text (str): The encrypted text to be decrypted.
    -   depth (int): The depth used for decryption.

    Returns:
    -   str: The decrypted text.
    """

    # If the length of the cipher text is less than the depth, return the cipher text
    if len(cipher_text) < depth:
        return cipher_text

    cipher_text_length = len(cipher_text)  # length of the cipher text

    # Divide the cipher text into chunks of length equal to the length of the cipher text divided by the depth
    if cipher_text_length % depth == 0:
        # Calculate the chunk size
        chunk_size = cipher_text_length // depth

        cipher_text_chunks = [
            cipher_text[i : i + chunk_size]
            for i in range(0, cipher_text_length, chunk_size)
        ]
    # Divide the cipher text into chunks of length equal to the length of the cipher text divided by the depth + 1
    else:
        # Calculate the chunk size
        chunk_size = cipher_text_length // depth + 1

        cipher_text_chunks = [
            cipher_text[i : i + chunk_size]
            for i in range(0, cipher_text_length, chunk_size)
        ]

    plain_text = ""  # decrypted text is stored in this variable

    # Loop through each character in the plain text
    for i in range(chunk_size):
        # Loop through each chunk in the cipher text
        for j in range(depth):
            # If the index is out of range, continue
            try:
                plain_text += cipher_text_chunks[j][i]
            except IndexError:
                continue

    return plain_text  # return the decrypted text


# Get the depth and plain text from the user
depth = int(input("Enter the depth: "))
plain_text_input = input("Enter the plain text: ")

# Encrypt the plain text using the Rail Fence cipher algorithm
cipher_text = rail_encrypt(plain_text_input, depth)
plain_text = rail_decrypt(cipher_text, depth)

# Print the encrypted and decrypted text
print("Encrypted text:", cipher_text)
print("Decrypted text:", plain_text)
