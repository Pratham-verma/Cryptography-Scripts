#!/usr/bin python3

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def map_to_charset(num):
    if num >= 1 and num <= 26:
        return chr(num + 64)  # Map to uppercase alphabet (A-Z)
    elif num >= 27 and num <= 36:
        return chr(num + 21)  # Map to decimal digits (0-9)
    elif num == 37:
        return '_'  # Map 37 to underscore
    else:
        return None

def decrypt_message(ciphertext):
    decrypted_message = ""
    for num in ciphertext:
        inverse = mod_inverse(num, 41)
        mapped_char = map_to_charset(inverse)
        if mapped_char:
            decrypted_message += mapped_char
        else:
            decrypted_message += '?'  # Placeholder for unmapped characters
    return decrypted_message

def main():
    ciphertext = [22,3, 28, 26, 16, 9, 26, 24, 23, 10, 36, 4, 16, 31, 10, 31 ,1, 31, 1, 1, 14, 1, 1]
    decrypted_message = decrypt_message(ciphertext)
    print("Decrypted message:")
    print("picoCTF{" + decrypted_message + "}")

if __name__ == "__main__":
    main()

