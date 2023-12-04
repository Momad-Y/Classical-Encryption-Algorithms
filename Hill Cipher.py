import numpy as np  # Import numpy for matrix operations
import math  # Import math for square root function


def initialize_matrices(key_text: str, text: str):
    """
    Initializes the key and plain matrices for the Hill Cipher encryption.

    Args:
    -   key_text (str): The key text used for encryption.
    -   text (str): The plain text to be encrypted.

    Returns:
    -   tuple: A tuple containing the key matrix and the plain matrix.
    Raises:
    -   ValueError: If the key length is not a perfect square or if the length of the cipher text is not a multiple of the matrix size.
    """

    matrix_size = math.sqrt(len(key_text))  # Calculate the matrix size

    # If the matrix size is not an integer, the key length is not a perfect square
    if matrix_size != int(matrix_size):
        raise ValueError("The key length must be a perfect square")

    matrix_size = int(matrix_size)  # Convert the matrix size to an integer

    # If the length of the cipher text is not a multiple of the matrix size, the cipher text cannot be encrypted
    if len(text) % matrix_size != 0:
        raise ValueError(
            "The length of the cipher text must be a multiple of the matrix size"
        )

    # Convert the key and cipher text to uppercase
    key_text = key_text.upper()
    text = text.upper()

    # Convert the key and cipher text to number representations using the ASCII table
    key_text = [ord(char) - 65 for char in key_text]
    text = [ord(char) - 65 for char in text]

    # Convert the key matrix to a numpy array using the matrix size
    key_matrix = np.array(list(key_text)).reshape(matrix_size, matrix_size)

    # Convert the cipher matrix to a numpy array using the matrix size and transpose it
    plain_matrix = np.array(list(text)).reshape(len(text) // matrix_size, matrix_size).T

    # Return the key and cipher matrices
    return key_matrix, plain_matrix


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


def hill_encrypt(key_text: str, plain_text: str):
    """
    Encrypts the given cipher text using the Hill Cipher algorithm.

    Parameters:
    -   key_text (str): The key text used for encryption.
    -   plain_text (str): The plain text to be encrypted.

    Returns:
    -   tuple: A tuple containing the encrypted text as a string and the encrypted matrix.
    """

    # Initialize the key and cipher matrices
    key_matrix, plain_matrix = initialize_matrices(key_text, plain_text)

    # Multiply the key matrix with the cipher matrix and take the modulo 26
    cipher_matrix = np.dot(key_matrix, plain_matrix) % 26

    # Convert the hill matrix to a string representation
    cipher_str = "".join([chr(char + 65) for char in cipher_matrix.flatten()])

    # Return the hill matrix
    return cipher_str, cipher_matrix


def hill_decrypt(key_text: str, cipher_text: str):
    """
    Decrypts the given cipher text using the Hill Cipher algorithm.

    Parameters:
    -   key_text (str): The key text used for decryption.
    -   cipher_text (str): The cipher text to be decrypted.

    Returns:
    -   tuple: A tuple containing the decrypted text as a string and the decrypted matrix.
    """

    # Initialize the key and cipher matrices
    key_matrix, cipher_matrix = initialize_matrices(key_text, cipher_text)

    # Calculate the determinant of the key matrix
    key_matrix_det = np.linalg.det(key_matrix)

    # If the determinant is 0, the key matrix is singular and the inverse does not exist
    if key_matrix_det == 0:
        raise ValueError("The key matrix is singular")

    # Calculate the inverse of the determinant of the key matrix
    key_matrix_det_mod = key_matrix_det % 26
    key_matrix_det_inv = mod_inverse(key_matrix_det_mod, 26)

    # If the determinant is not coprime with 26, the inverse does not exist
    if key_matrix_det_inv == -1:
        raise ValueError("The key matrix is not invertible")

    # Calculate the inverse of the key matrix
    key_matrix_cofactor = key_matrix_det * np.linalg.inv(key_matrix.T)
    key_matrix_adjugate = key_matrix_cofactor.T * key_matrix_det_inv
    key_matrix_inv = key_matrix_adjugate % 26

    # Change the datatype of the key matrix to integer
    for i in range(len(key_matrix_inv)):
        for j in range(len(key_matrix_inv)):
            key_matrix_inv[i][j] = int(round(key_matrix_inv[i][j], 1))

    key_matrix_inv = key_matrix_inv.astype(int)

    # Multiply the inverse of the key matrix with the cipher matrix and take the modulo 26
    plain_matrix = np.dot(key_matrix_inv, cipher_matrix) % 26

    # Convert the hill matrix to a string representation
    plain_str = "".join([chr(char + 65) for char in plain_matrix.flatten()])

    # Return the hill matrix
    return plain_str, plain_matrix


# Get the key text and plain text from the user
key_text_input = input("Enter the key text: ")
plain_text_input = input("Enter the plain text: ")

# Encrypt the plain text using the Hill Cipher algorithm
cipher_str, cipher_matrix = hill_encrypt(key_text_input, plain_text_input)

# Print the encrypted text and matrix
print("Encrypted text:", cipher_str)
print("Encrypted matrix:\n", cipher_matrix.flatten().T)
print()

# Decrypt the cipher text using the Hill Cipher algorithm
plain_str, plain_matrix = hill_decrypt(key_text_input, cipher_str)

# Print the decrypted text and matrix
print("Decrypted text:", plain_str)
print("Decrypted matrix:\n", plain_matrix.flatten().T)
