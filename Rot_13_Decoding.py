def rot13(text):
    result = ''
    for char in text:
        if char.isalpha():
            # Determine whether the character is uppercase or lowercase
            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')
            # Apply ROT13 transformation
            offset = (ord(char) - start + 13) % 26
            result += chr(start + offset)
        else:
            result += char
    return result

def main():
    plaintext = "cvpbPGS{P7e1S_54I35_71Z3}"
    encrypted_text = rot13(plaintext)
    print("Encrypted text:", encrypted_text)

if __name__ == "__main__":
    main()

