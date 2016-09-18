# converts numbers from decimal to the base supplied
def convert_number_from_dec(num, base):

    if num == 0:
        return ""
    elif num == 1:
        return str(num)
    else:
        result = str(convert_number_from_dec(num // base, base)) + number_to_letter(num % base)
        return result


# converts numbers to decimal from the base supplied
def convert_number_to_dec(num, base):

    result = 0

    # todo: fix the rest of this - done?
    if num == "0":
        return 0
    else:
        for x in num:
            result = (result + letter_to_number(x)) * base

    return result


# convert a number to a letter (bases between dec and hex)
def number_to_letter(num):

    if 0 <= num < 10:
        return str(num)
    elif num < 16:
        # convert from decimal to hex etc.
        return chr(ord('A') + num % 10)
    # elif num < 61:
        # return chr(ord('a') + num % 10)


# convert a letter to a number (bases between dec and hex)
def letter_to_number(num):
    # todo: fix the rest of this - done?
    if "0" <= num <= "9":
        return int(num)
    else:
        # convert from decimal to hex etc.
        return ord(num) - ord("A")
    # elif num < 61:
        # return chr(ord('a') + num % 10)


# ensure loop runs once
num_str = "placeholder text"
base_str = "placeholder text"

# validate inputs
while not num_str.isdigit():
    num_str = input("Enter a number to be converted (positive integer): ")

while not base_str.isdigit():
    base_str = input("Enter the base to convert to: ")

num_int = int(num_str)
base_int = int(base_str)


if 0 < base_int <= 16:
    print(convert_number_from_dec(num_int, base_int))
else:
    print("Unable to do conversion - base must be a positive integer between 1 and 16!")


