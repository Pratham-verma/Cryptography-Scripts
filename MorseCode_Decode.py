MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
    '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
    '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z',
    '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7',
    '---..': '8', '----.': '9', '-----': '0',
    '/': ' '
}

def decode_morse(encoded_text):
    words = encoded_text.split(' / ')
    decoded_text = ''
    for word in words:
        letters = word.split()
        for letter in letters:
            if letter in MORSE_CODE_DICT:
                decoded_text += MORSE_CODE_DICT[letter]
        decoded_text += ' '
    return decoded_text.strip()

def main():
    file_path = input("Enter the file path to the encoded Morse code file: ")
    try:
        with open(file_path, 'r') as file:
            encoded_text = file.read()
            decoded_text = decode_morse(encoded_text)
            print("Decoded text:")
            print(decoded_text)
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")

if __name__ == "__main__":
    main()

