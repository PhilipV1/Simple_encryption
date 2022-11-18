
def encrypt_caesar(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isupper():
            ciphertext += chr((ord(char) + key - 65) % 26 + 65)
        elif char.islower():
            ciphertext += chr((ord(char) + key - 97) % 26 + 97)
        else:
            ciphertext += " "
    
    return ciphertext


def decrypt_caesar(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.isupper():
            plaintext += chr((ord(char) - key - 65) % 26 + 65)
        elif char.islower():
            plaintext += chr((ord(char) - key - 97) % 26 + 97)
        else:
            plaintext += " "
    
    return plaintext


def get_order(key):
    orderedtxt = "".join(sorted(key))
    columnorder = []
    letter_pos = dict()

    for i, c in enumerate(orderedtxt):
        letter_pos.update({c: i})
    
    for char in key:
        columnorder.append(letter_pos.get(char))
    print(f"Column order: {columnorder}")
    return columnorder


def encrypt_transpos(plaintext, key):
    columns = len(key)
    rows = len(plaintext) // columns
    plaintext = plaintext.replace(" ", "")
    plainlist = []
    plainlist[:0] = plaintext
    column_order = get_order(key)
    ciphertext = ""
    matrix = [[0 for i in range(columns)] for j in range(rows)]
    print(matrix)

    for c in range(columns):
        for r in range(rows):
            if len(plainlist) > 0:
                matrix[r][c] = plainlist[0]
                plainlist.pop(0)
            else:
                matrix[r][c] = ""
    print(f"Matrix: {matrix}")
    for c in column_order:
        for r in range(rows):
            ciphertext += matrix[c][r]

    return ciphertext


def decrypt_transpos(plaintext, key):
    pass


def main():
    # plaintxt = input("Please enter message you want to encrypt: ")
    # encrypted_msg = encrypt_caesar(plaintxt, 5)
    # decrypt_msg = decrypt_caesar(encrypted_msg, 5)
    
    # print(f"Plaintext: {plaintxt}")
    # print(f"Encrypted message substitution: {encrypted_msg}")
    # print(f"Decrypted message substitution: {decrypt_msg}")

    # print(f"Encrypted transposition: ")
    plain = "We are discovered save yourself"
    key = "author"

    cipher = encrypt_transpos(plain, key)
    print(f"Ciphertext: {cipher}")


if __name__ == "__main__":
    main()