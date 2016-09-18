
def convert_number(num, base):

    if num == 0:
        return ""
    if num == 1:
        return str(num)
    else:
        result = str(convert_number(num // base, base)) + get_digit(num % base)
        return result


def get_digit(num):
    if 0 <= num < 10:
        return str(num)
    elif num < 16:
        return chr(ord('A') + num % 10)
    # elif num < 61:
        # return chr(ord('a') + num % 10)


num_str = input("Enter a number to be converted: ")
base_str = input("Enter the base to convert to: ")

num_int = int(num_str)
base_int = int(base_str)


if 0 < base_int <= 16:
    print(convert_number(num_int, base_int))
else:
    print("Unable to do conversion - base must be a positive integer between 1 and 16!")


