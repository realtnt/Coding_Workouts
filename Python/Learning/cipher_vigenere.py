def calc_shift(key_letter):
    key_letter = key_letter.upper()
    shift = ord(key_letter) - ord('A')
    return shift


def vig_encrypt(text, key, ignore_non_text=False):
    text = text.upper()
    key = key.upper()

    encrypted_text = []
    key_counter = 0
    for letter in text:
        if ord(letter) not in range(ord('A'), ord('Z')+1):
            if ignore_non_text:
                continue
            else:
                encrypted_text.append(letter)
                continue
        shift_by = (ord(letter)-ord('A') +
                    calc_shift(key[key_counter % len(key)])) % 26
        shift_to = chr(ord('A') + shift_by)
        encrypted_text.append(shift_to)
        key_counter += 1
    return "".join(encrypted_text)


def vig_decrypt(text, key, ignore_non_text=False):
    text = text.upper()
    key = key.upper()

    decrypted_text = []
    key_counter = 0
    for letter in text:
        if ord(letter) not in range(ord('A'), ord('Z')+1):
            if ignore_non_text:
                continue
            else:
                decrypted_text.append(letter)
                continue
        shift_by = (ord(letter)-ord('A') -
                    calc_shift(key[key_counter % len(key)])) % 26
        shift_to = chr(ord('A') + shift_by)
        decrypted_text.append(shift_to)
        key_counter += 1
    return "".join(decrypted_text)


the_key = "BRITAIN"
text_to_encrypt = "WE SHALL NEVER SURRENDER"
cipher_text = vig_encrypt(text_to_encrypt, the_key)

print(cipher_text)
print(vig_decrypt(cipher_text, the_key))
