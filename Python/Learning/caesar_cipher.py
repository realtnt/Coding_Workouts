letter_frequencies = [8.04, 1.48, 3.34, 3.82, 12.49, 2.40, 1.87, 5.05, 7.57, 0.16, 0.54,
                      4.07, 2.51, 7.23, 7.64, 2.14, 0.12, 6.28, 6.51, 9.28, 2.73, 1.05, 1.68, 0.23, 1.66, 0.09]
other_chars_passthrough = True
# Checks for invalid input.


def safe_input(message, input_type=str, lower_limit=None, upper_limit=None, empty_allowed=None):
    while True:
        user_input = input(message)
        if user_input == "" and empty_allowed == True:
            return ""
        try:
            if user_input == "" and empty_allowed == None:
                raise ValueError("Empty string not allowed")
            if input_type == int:
                user_input = int(user_input)
            elif input_type == float:
                user_input = float(user_input)
            if lower_limit != None and user_input < lower_limit or upper_limit != None and user_input > upper_limit:
                raise ValueError("Not in range!")
        except ValueError:
            print("Input not valid!")
        else:
            return user_input

# encrypts text using key
# non text characters are passed through unchanged


def encrypt(text, key):
    text = text.upper()
    encrypted = []
    for letter in text:
        encrypted_letter = ord(letter) + key
        if ord(letter) not in range(ord('A'), ord('Z')+1):
            if other_chars_passthrough:
                encrypted.append(letter)
            else:
                continue
        elif encrypted_letter > ord('Z'):
            encrypted.append(chr(encrypted_letter - 26))
        else:
            encrypted.append(chr(encrypted_letter))
    return "".join(encrypted)

# decrypts a text using the key
# non text characters are passed through unchanged


def decrypt_with_key(text, key):
    text = text.upper()
    decrypted = []
    for letter in text:
        decrypted_letter = ord(letter) - key
        if ord(letter) not in range(ord('A'), ord('Z')+1):
            decrypted.append(letter)
        elif decrypted_letter < ord('A'):
            decrypted.append(chr(decrypted_letter + 26))
        else:
            decrypted.append(chr(decrypted_letter))
    return "".join(decrypted)

# takes some text and uses decrypt_with_key to return a list with all possible decryptions


def decrypt_brute_force(text):
    decrypt_list = []
    for key in range(1, 26):
        decrypt_list.append(decrypt_with_key(text, key))
    return decrypt_list

# takes a word and returns its the word probability ignoring non TEXT characters


def decrypt_analysis(word):
    probability = 0
    for letter in word:
        if ord(letter) in range(ord('A'), ord('Z')+1):
            probability += letter_frequencies[ord(letter) - ord('A')]
    return probability

# takes a list with of possible description and returns a list of possible decryptions
# sorted from highest to lowest probability. possibilities controls how many possible
# solutions to return


def decrypt_list_analysis(decrypt_list, possibilities):
    probability_list = []
    for word in decrypt_list:
        probability_list.append(decrypt_analysis(word))

    sorted_prob_list = probability_list.copy()
    sorted_prob_list.sort(reverse=True)

    sorted_list_by_probability = []
    for i in sorted_prob_list:
        index = 0
        for k in probability_list:
            if i == k:
                sorted_list_by_probability.append(decrypt_list[index])
            index += 1
        if len(sorted_list_by_probability) == possibilities:
            break

    return sorted_list_by_probability


def write_to_file(filename, text):
    try:
        f = open(filename)
    except FileNotFoundError:
        file_exists = False
    else:
        file_exists = True

    if file_exists:
        overwrite = get_user_command(
            "File exists. Overwrite? (Y/N): ", ["y", "n"])
        if overwrite == "n":
            return False

    with open(filename, "w") as f:
        f.write(text)
    return True


def read_from_file(filename):
    try:
        f = open(filename)
    except FileNotFoundError:
        print("File does not exist!")
        return False
    else:
        text = f.read()
        f.close()
    return text


def get_user_command(question_text, valid_responses_list):
    user_input = ""
    while user_input not in valid_responses_list:
        user_input = safe_input(question_text).lower()
        if user_input in valid_responses_list:
            return user_input
        else:
            print("Huh?")


# Menu loop
while True:
    text_to_encrypt = ""
    command = get_user_command(
        "(E)ncrypt or (D)ecrypt? (Q to quit, S for settings): ", ["e", "d", "q", "s"])
    if command == "e":
        while True:
            command2 = get_user_command(
                "Load (F)ile or (I)nput text (B to go back): ", ["f", "i", "b"])
            if command2 == "f":
                input_file_to_encrypt = safe_input("Enter filename: ")
                text_to_encrypt = read_from_file(input_file_to_encrypt)
                if text_to_encrypt == False:
                    continue
                key = safe_input("Enter a key (an integer value between 1 and 25): ",
                                 int, lower_limit=1, upper_limit=25)
                print(f"Input text:\n\n{text_to_encrypt}")
                print("-"*20)
                encrypted = "".join(encrypt(text_to_encrypt, key))
                print(f"Your ciphertext is:\n\n{encrypted}")
                print("*"*20)
                while True:
                    command3 = get_user_command(
                        "Save file? (Y/N): ", ["y", "n"])
                    if command3 == "y":
                        output_file = safe_input("Enter filename: ")
                        write_to_file(output_file, encrypted)
                    else:
                        break
                    break
            elif command2 == "i":
                word_to_encrypt = safe_input(
                    "Enter some text to encrypt: ").upper()
                key = safe_input("Enter a key (an integer value between 1 and 25): ",
                                 int, lower_limit=1, upper_limit=25)
                encrypted = "".join(encrypt(word_to_encrypt, key))
                print(f"Your ciphertext is: {encrypted}")
            elif command2 == "b":
                break
    elif command == "d":
        while True:
            command2 = get_user_command(
                "Load (F)ile or (I)nput text (B to go back): ", ["f", "i", "b"])
            if command2 == "b":
                break
            elif command2 == "f":
                input_file_to_decrypt = safe_input("Enter filename: ")
                text_to_decrypt = read_from_file(input_file_to_decrypt)
                if text_to_decrypt == False:
                    continue
            elif command2 == "i":
                text_to_decrypt = safe_input(
                    "Enter some text to decrypt: ").upper()
            while True:
                command3 = input(
                    "With (K)ey, b(R)ute force, letter (F)requency (B to go back): ").lower()
                if command3 == "b":
                    break
                if command3 == "k":
                    key = safe_input("Enter a key (an integer value between 1 and 25): ",
                                     int, lower_limit=1, upper_limit=25)
                    decrypted_text = ''.join(
                        decrypt_with_key(text_to_decrypt, key))
                elif command3 == "r":
                    number_of_results = safe_input(
                        "How many results do you want to see? (1-25): ", int, lower_limit=1, upper_limit=25)
                    separator_text = "\n\n"+"*-"*40+"\n\n"
                    decrypted_text = decrypt_brute_force(text_to_decrypt)
                    print("The decrypted text is:\n\n")
                    for i in range(0, number_of_results+1):
                        print(f"--> KEY: {i+1}")
                        print(decrypted_text[i])
                        print(separator_text)
                    break
                elif command3 == "f":
                    decrypted_text = ''.join(
                        decrypt_list_analysis(decrypt_brute_force(text_to_decrypt), 1))
                print("The decrypted text is:\n\n")
                print(decrypted_text)
                while True:
                    command4 = get_user_command(
                        "Save file? (Y/N): ", ["y", "n"])
                    if command4 == "y":
                        output_file = safe_input("Enter filename: ")
                        write_to_file(output_file, decrypted_text)
                    else:
                        break
                    break
    elif command == "s":
        char_passthrough = get_user_command(
            "Remove non letter characters? ", ["y", "n"])
        if char_passthrough == "y":
            other_chars_passthrough = False
        else:
            other_chars_passthrough = True
    elif command == "q":
        print("Bye bye")
        break
