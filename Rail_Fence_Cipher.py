def encrypt_rail_fence(text, key):
    rail = [['\n' for j in range(len(text))] for i in range(key)]


    row, col = 0, 0
    direction = False
    
    for char in text:
        if row == 0 or row == key - 1:
            direction = not direction
        rail[row][col] = char
        col += 1

        if direction:
            row += 1
        else:
            row -= 1
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])

    return ''.join(result)


def decrypt_rail_fence(ciphertext, key):
    rail = [['\n' for j in range(len(ciphertext))] for i in range(key)]

    row, col = 0, 0
    direction = False

    for i in range(len(ciphertext)):
        if row == 0 or row == key - 1:
            direction = not direction
        rail[row][col] = '*'
        col += 1

        if direction:
            row += 1
        else:
            row -= 1

    index = 0
    for i in range(key):
        for j in range(len(ciphertext)):
            if (rail[i][j] == '*') and (index < len(ciphertext)):
                rail[i][j] = ciphertext[index]
                index += 1

    result = []
    row, col = 0, 0
    direction = False
    for j in range(len(ciphertext)):
        if row == 0:
            direction = True
        if row == key - 1:
            direction = False

        if rail[row][col] != '*':
            result.append(rail[row][col])
            col += 1

        if direction:
            row += 1
        else:
            row -= 1

    return ''.join(result)


# Example usage:
plaintext = "WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_83F6D8D7"
key = 4
encrypted_text = encrypt_rail_fence(plaintext, key)
print("Encrypted:", encrypted_text)
decrypted_text = decrypt_rail_fence(encrypted_text, key)
print("Decrypted:", decrypted_text)

