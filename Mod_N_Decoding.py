def decrypt_message(ciphertext, modulus, charset):
    decrypted_message = ""
    for num in ciphertext:
        mapped_char = charset[num % modulus]
        decrypted_message += mapped_char
    return decrypted_message

def main():
    modulus = 41
    charset = {i: chr(i + 64) if i >= 1 and i <= 26 else chr(i + 21) if i >= 27 and i <= 36 else '_' for i in range(modulus)}
    ciphertext = [7, 32, 18, 2, 14, 6, 22, 15, 30, 13, 19, 23, 27, 4, 28, 13, 4, 27, 13, 32, 15, 6, 16, 4, 19, 4, 2, 14, 10, 31, 21, 30, 5, 32, 7, 27, 29, 28, 13, 1, 6, 15, 27, 3, 22, 16, 17, 32, 12, 13, 4]
    decrypted_message = decrypt_message(ciphertext, modulus, charset)
    print("Decrypted message:")
    print("picoCTF{" + decrypted_message + "}")

if __name__ == "__main__":
    main()

