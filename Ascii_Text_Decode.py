def ascii_to_plain_text(ascii_text):
    plain_text = ''.join(chr(int(ascii_char, 16)) for ascii_char in [ascii_text[i:i+2] for i in range(0, len(ascii_text), 2)])
    return plain_text

ascii_text = input("Enter the ASCII text: ")

plain_text = ascii_to_plain_text(ascii_text)

print("Plain text:", plain_text)

