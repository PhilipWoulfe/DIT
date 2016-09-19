# converts numbers from decimal to the base supplied - returns string
def convert_number_from_dec(num_int, base):

    num_int = int(num_int)

    if num_int == 0:
        return ""
    elif num_int == 1:
        return str(num_int)
    else:
        result = str(convert_number_from_dec(num_int // base, base)) + number_to_letter(num_int % base)
        return result


# converts numbers to decimal from the base supplied - returns int
def convert_number_to_dec(num_str, base):

    result = 0
    counter = len(num_str) - 1

    if base == 10:
        result = int(num_str)
    elif num_str == "0":
        result = 0
    else:
        for x in num_str:
            result += letter_to_number(x) * base ** counter
            counter -= 1

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

    if "0" <= num <= "9":
        return int(num)
    else:
        # convert from decimal to hex etc.
        return (ord(num) - ord("A")) + 10
    # elif num < 61:
        # return chr(ord('a') + num % 10)


# ensure loop runs once
base_from_str = "placeholder text"
base_to_str = "placeholder text"

# validate inputs
while not base_from_str.isdigit():
    base_from_str = input("Enter the base to convert from (base must be between 2 and 16): ")

while not base_to_str.isdigit():
    base_to_str = input("Enter the base to convert to (base must be between 2 and 16): ")

# todo validate input based on base from string
num_str = input("Enter a number to be converted (positive integer): ")

base_from_int = int(base_from_str)
base_to_int = int(base_to_str)


if 1 < base_from_int < 17:
    output = convert_number_to_dec(num_str, base_from_int)
else:
    print("Unable to do conversion - base from must be a positive integer between 1 and 16!")

if 1 < base_to_int < 17:
    output = str(convert_number_from_dec(int(output), base_to_int))
else:
    print("Unable to do conversion - base from must be a positive integer between 1 and 16!")

print(num_str, "in base", base_from_int, "is", output, "in base", base_to_str)
