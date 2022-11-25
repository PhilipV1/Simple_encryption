def encrypt_caesar(plaintext, key):
    '''Caesar cipher encryption. Given a key the encryption
    will add the key value to each plaintext letters ASCII value'''
    ciphertext = ""
    for char in plaintext:
        # Subtract 65/95 to order the letter from 0-25
        # Then add 65/95 after the calculation to account for ASCII values
        if char.isupper():
            ciphertext += chr((ord(char) + key - 65) % 26 + 65)
        elif char.islower():
            ciphertext += chr((ord(char) + key - 97) % 26 + 97)
        else:
            ciphertext += " "

    return ciphertext


def decrypt_caesar(ciphertext, key):
    '''Caesar cipher decryption. given a key the decryption
    will subtract the key value to each ciphertext letters ASCII value'''
    plaintext = ""
    for char in ciphertext:
        # Subtract 65/95 to order the letter from 0-25
        # Then add 65/95 after the calculation to account for ASCII values
        if char.isupper():
            plaintext += chr((ord(char) - key - 65) % 26 + 65)
        elif char.islower():
            plaintext += chr((ord(char) - key - 97) % 26 + 97)
        else:
            plaintext += " "

    return plaintext


def get_order(key):
    '''Gets the order of the columns based on the
    alphabetical order of the letters in the keyword'''
    orderedtxt = "".join(sorted(key))
    columnorder = []
    letter_pos = dict()

    for i, c in enumerate(key):
        letter_pos.update({c: i})

    for char in orderedtxt:
        columnorder.append(letter_pos.get(char))

    return columnorder


def encrypt_transpos(plaintext, key):
    '''Transposition encryption base on a keyword'''
    # Initialize columns, rows, plaintext list and matrix
    columns = len(key)
    # Using negative integer division instead of ceil method
    rows = (len(plaintext) * -1) // columns
    rows *= -1
    plainlist = []
    plainlist[:0] = plaintext
    column_order = get_order(key)
    ciphertext = ""
    matrix = [[0 for i in range(columns)] for j in range(rows)]
    # Write plaintext in the matrix left-right, top-bottom
    for r in range(rows):
        for c in range(columns):
            if len(plainlist) > 0:
                matrix[r][c] = plainlist[0]
                plainlist.pop(0)
            else:
                matrix[r][c] = " "
    # Take out cipher text in keyword based column order
    for c in column_order:
        for r in range(rows):
            ciphertext += matrix[r][c]

    return ciphertext


def decrypt_transpos(ciphertext, key):
    '''Transposition decryption based on a keyword'''
    # Initialize columns, rows, ciphertext list and matrix
    columns = len(key)
    # Using negative integer division instead of ceil method
    rows = (len(ciphertext) * -1) // columns
    rows *= -1
    column_order = get_order(key)
    cipherlist = []
    cipherlist[:0] = ciphertext
    plaintext = ""
    matrix = [[0 for i in range(columns)] for j in range(rows)]

    # Write the ciphertext in the keyword based column order
    for c in column_order:
        for r in range(rows):
            if len(cipherlist) > 0:
                matrix[r][c] = cipherlist[0]
                cipherlist.pop(0)
            else:
                matrix[r][c] = " "
    # Read the plaintext from left-right, top-bottom
    for r in range(rows):
        for c in range(columns):
            plaintext += matrix[r][c]

    return plaintext


def main():
    # plaintxt = input("Please enter message you want to encrypt: ")
    # encrypted_msg = encrypt_caesar(plaintxt, 5)
    # decrypt_msg = decrypt_caesar(encrypted_msg, 5)

    # print(f"Plaintext: {plaintxt}")
    # print(f"Encrypted message substitution: {encrypted_msg}")
    # print(f"Decrypted message substitution: {decrypt_msg}")

    # print(f"Encrypted transposition: ")
    plain = "We are discovered save yourself"
    key = "help"

    print(f"Plaintext: {plain}")
    cipher = encrypt_transpos(plain, key)
    print(f"Ciphertext: {cipher}")
    deciphered = decrypt_transpos(cipher, "help")
    print(f"Decrypted plaintext: {deciphered}")


if __name__ == "__main__":
    main()
