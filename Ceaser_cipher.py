def encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            
            base = ord('A') if char.isupper() else ord('a')
            p = ord(char) - base
            e = (p + key) % 26
            new_char = chr(e + base)
            result += new_char.lower() if char.isupper() else new_char.upper()
        else:
            result += char
    return result

def decrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            p = ord(char) - base
            d = (p - key) % 26
            new_char = chr(d + base)
            result += new_char.lower() if char.isupper() else new_char.upper()
        else:
            result += char
    return result

def main():
    choice = input("Choose an option (encrypt/decrypt): ").strip().lower()
    if choice not in ['encrypt', 'decrypt']:
        print("Invalid choice.")
        return

    text = input("Enter the text: ")
    
    try:
        key = int(input("Enter the key (integer): "))
    except ValueError:
        print("Key must be an integer.")
        return

    if choice == 'encrypt':
        encrypted_text = encrypt(text, key)
        print("Encrypted text:", encrypted_text)
    else:
        decrypted_text = decrypt(text, key)
        print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
