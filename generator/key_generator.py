import random

secret_key = "3141-5026-5358-0703-2384"
alphabet_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZZ"

# each digit of the secret key is randomly encoded to one of three letters
# for example 0 is randomly encoded to A or B or C; 1 to D or E or F; etc.


def encode_digit_to_letter(in_digit):
    if (in_digit == '-'):
        return('-')
    else:
        offset = int(in_digit)*3 + random.randint(0, 2)
        return alphabet_string[offset]

# each letter is decoded back to a digit


def decode_letter_to_digit(in_letter):
    if (in_letter == '-'):
        return('-')
    else:
        offset = alphabet_string.index(in_letter)
        return str(offset//3)


def generate_key():
    license_key = ""
    for x in secret_key:
        license_key = license_key + encode_digit_to_letter(x)
    return license_key


def validate_key(license_key):
    decode_key = ""
    for x in license_key:
        decode_key = decode_key + decode_letter_to_digit(x)
    if (decode_key == secret_key):
        return True
    else:
        return False


# test generating and validating 20 keys
for _ in range(20):
    key = generate_key()
    print(key)
    print(validate_key(key))
