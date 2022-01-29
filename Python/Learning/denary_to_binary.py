user_input = -1
# keep asking for a number if user does not enter a number between 0 and 255
while user_input == -1:
    user_input = input("Enter number between 0 and 255: ")
    if int(user_input) < 0 or int(user_input) > 255:
        print("Out of range.")
        user_input = -1

# to convert dec to bin we divide the decimal number by two and store the remainder
# which is going to be 0 or 1 and then write out the remainders in reverse order.
dec_value = int(user_input)
binary = []
for i in range(8):  # for loop so that we always get 8 bits
    remainder = dec_value % 2  # get the remainder
    binary.append(remainder)  # append it to the binary list
    dec_value //= 2  # int divide the decimal value by two
binary.reverse()  # reverse it
# print it joining it to make it look nice
print(f"{user_input} = 0b{''.join(map(str, binary))}")

# check the we are getting valid binary numbers
bin_value = "invalid"
while bin_value == "invalid":
    bin_value = input("Enter an 8-bit binary number: ")
    if len(bin_value) != 8:
        bin_value = "invalid"
    for bit in bin_value:
        if bit != '0' and bit != '1':
            bin_value = "invalid"
            continue
    if bin_value == "invalid":
        print("Not a valid 8-bit number!")
# we are going to multiply each digit to the corresponding power of 2 for its place
dec_value = 0
for i in range(8):
    # 7-i because the values are in reverse [0] is the MSB
    dec_value += int(bin_value[i])*2**(7-i)
print(f"0b{bin_value} = {dec_value}")
