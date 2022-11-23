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
    # Back
    # Orderedtxt = "abck"
    #dict = {a: 0, b: 1, c: 2, k: 3}
    # Jämför "abck"
    orderedtxt = "".join(sorted(key))
    columnorder = []
    letter_pos = dict()

    for i, c in enumerate(key):
        letter_pos.update({c: i})
    
    for char in orderedtxt:
        columnorder.append(letter_pos.get(char))

    return columnorder


def encrypt_transpos(plaintext, key):
    columns = len(key)

    rows = (len(plaintext) * -1) // columns
    rows *= -1
    plainlist = []
    plainlist[:0] = plaintext
    column_order = get_order(key)
    ciphertext = ""
    matrix = [[0 for i in range(rows)] for j in range(columns)]

    for r in range(rows):
        for c in range(columns):
            if len(plainlist) > 0:
                matrix[c][r] = plainlist[0]
                plainlist.pop(0)
            else:
                matrix[c][r] = " "

    for c in column_order:
        for r in range(rows):
            ciphertext += matrix[c][r]

    return ciphertext


def decrypt_transpos(ciphertext, key):
    columns = len(key)
    rows = (len(ciphertext) * -1) // columns
    rows *= -1
    column_order = get_order(key)
    cipherlist = []
    cipherlist[:0] = ciphertext
    plaintext = ""
    matrix = [[0 for i in range(rows)] for j in range(columns)]

    for c in column_order:
        for r in range(rows):
            if len(cipherlist) > 0:
                matrix[c][r] = cipherlist[0]
                cipherlist.pop(0)
            else:
                matrix[c][r] = " "
    
    for r in range(rows):
        for c in range(columns):
            plaintext += matrix[c][r]

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
