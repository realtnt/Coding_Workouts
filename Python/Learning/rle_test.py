import re


def rle_encode3(a_string):
    rle_string = ""
    split_string = re.findall(r'((.)\2*)', a_string)
    for repeated in split_string:
        rle_string += repeated[1] + str(len(repeated[0]))
    return rle_string


a_string = "BBBBCCCDDDDDD"
print(rle_encode3(a_string))
