def encrypt_message(plaintext, modulus):
    ciphertext = []
    for char in plaintext:
        if char.isalpha():
            num = ord(char.upper()) - 64  # Convert character to its corresponding number (A=1, B=2, ..., Z=26)
            ciphertext.append(num % modulus)
        elif char.isdigit():
            num = int(char)
            if num >= 0 and num <= 9:
                ciphertext.append(num + 26)  # Map digits 0-9 to 27-36
        elif char == '_':
            ciphertext.append(37)  # Map underscore to 37
        else:
            print(f"Character '{char}' not supported. Skipping...")
    return ciphertext

def main():
    modulus = 41
    plaintext = "HELLO_WORLD123"
    ciphertext = encrypt_message(plaintext, modulus)
    print("Ciphertext:")
    print(ciphertext)

if __name__ == "__main__":
    main()

