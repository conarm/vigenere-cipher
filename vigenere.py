'''Encrypt or decrypt strings using an extended Vigenere Cipher.'''


def generate_key(plaintext, key):
    '''Take in the plaintext and the key.
    If the key is shorter than the plaintext, pad it out cyclically.
    '''
    key = list(key)
    if len(plaintext) != len(key):
        for i in range(len(plaintext) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)


def ext_vigenere(plaintext, key, option):
    '''Take in the text, the key and the option (encrypt or decrypt).
    If the option is encrypt, encrypt the text with the key and return it.
    If the option is decrypt, decrypt the text with the key and return it.
    '''
    key = generate_key(plaintext, key)
    text = ""
    if option == "encrypt":
        for letter in range(len(plaintext)):
            offset = ord(plaintext[letter]) - 32
            key_offset = ord(key[letter]) - 32
            letter_val = key_offset
            for _ in range(offset):
                letter_val += 1
                if letter_val == 95:
                    letter_val = 0
            text += chr(letter_val + 32)
    elif option == "decrypt":
        for i in range(len(plaintext)):
            offset = ord(plaintext[i]) - 32
            key_offset = ord(key[i]) - 32
            letter_val = offset
            for _ in range(key_offset):
                letter_val -= 1
                if letter_val == -1:
                    letter_val = 94
            text += chr(letter_val + 32)
    else:
        text = "Invalid option!"
    return text
