import string

ALPHABET = string.ascii_uppercase
BASE_CHAR = "A"


def get_shifted_char(character, shift):
    char_code = ord(character.upper())
    shifted_char = ord(BASE_CHAR) + ((char_code - ord(BASE_CHAR) + shift) % 26)
    return chr(shifted_char)


def caesar_encrypt(plaintext, key):
    plaintext = plaintext.upper()
    ciphertext = ""
    for char in plaintext:
        if char not in ALPHABET:
            ciphertext = ciphertext + char
        else:
            ciphertext = ciphertext + get_shifted_char(char, key)
    return ciphertext


def caesar_decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    plaintext = ""
    for char in ciphertext:
        if char not in ALPHABET:
            plaintext = plaintext + char
        else:
            plaintext = plaintext + get_shifted_char(char, -key)
    return plaintext


def calc_vigenere_shift(keyword, count):
    keyword = keyword.upper()
    key_length = len(keyword)
    current_shift = ord(keyword[count % key_length]) - ord(BASE_CHAR)
    return current_shift


def vigenere_encrypt(plaintext, keyword):
    plaintext = plaintext.upper()
    ciphertext = ""
    counter = 0
    for char in plaintext:
        key = calc_vigenere_shift(keyword, counter)

        if char not in ALPHABET:
            ciphertext = ciphertext + char
        else:
            ciphertext = ciphertext + get_shifted_char(char, key)
            counter += 1
    return ciphertext


def vigenere_decrypt(ciphertext, keyword):
    ciphertext = ciphertext.upper()
    plaintext = ""
    counter = 0
    for char in ciphertext:
        key = calc_vigenere_shift(keyword, counter)
        if char not in ALPHABET:
            plaintext = plaintext + char
        else:
            plaintext = plaintext + get_shifted_char(char, -key)
            counter += 1
    return plaintext


orig_text = "WE SHALL NEVER SURRENDER"
key = 3
keyword = "BRITAIN"

# CAESAR
encrypted = caesar_encrypt(orig_text, key)
print(encrypted)
decrypted = caesar_decrypt(encrypted, key)
print(decrypted)

# VIGENERE
encrypted = vigenere_encrypt(orig_text, keyword)
print(encrypted)
decrypted = vigenere_decrypt(encrypted, keyword)
print(decrypted)
