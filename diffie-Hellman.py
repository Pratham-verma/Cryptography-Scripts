def decrypt(ciphertext, shared_key):
    decrypted_text = ""
    for char_code in ciphertext:
        decrypted_char_code = char_code // shared_key
        decrypted_text += chr(decrypted_char_code)
    return decrypted_text

if __name__ == "__main__":
    ciphertext = [260307, 491691, 491691, 2487378, 2516301, 0, 1966764, 1879995, 1995687, 1214766, 0, 2400609, 607383, 144615, 1966764, 0, 636306, 2487378, 28923, 1793226, 694152, 780921, 173538, 173538, 491691, 173538, 751998, 1475073, 925536, 1417227, 751998, 202461, 347076, 491691]
    text_key = "trudeau"

    # Compute shared key using Diffie-Hellman key exchange algorithm
    p = 97
    g = 31
    a = 94
    b = 29
    u = pow(g, a, p)
    v = pow(g, b, p)
    shared_key = pow(v, a, p)  # Shared key computed by Alice
    b_key = pow(u, b, p)  # Shared key computed by Bob

    # Check if both shared keys match
    if shared_key == b_key:
        # Decrypting the ciphertext
        decrypted_text = decrypt(ciphertext, shared_key)
        print("Decrypted text:", decrypted_text)
    else:
        print("Invalid key")

