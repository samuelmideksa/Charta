import re


def isbn_validator(isbn):
    # Remove hyphens and spaces from the input
    isbn_without_sep = re.sub(r'[-\s]', '', isbn)

    # Regular expression pattern for ISBN-10 or ISBN-13
    isbn_regex = r'^\d{9}[\dXx]|\d{13}$'

    # Check if the input matches the ISBN pattern
    if not re.match(isbn_regex, isbn_without_sep):
        raise ValueError('Invalid ISBN format')

    # Check if the length of the input is either 10 or 13
    if len(isbn_without_sep) not in {10, 13}:
        raise ValueError('ISBN must be 10 or 13 digits long')

    # # If the input is ISBN-10, calculate the check digit
    # if len(isbn_without_sep) == 10:
    #     check_sum = sum((i + 1) * int(digit) for i, digit in enumerate(isbn_without_sep[:-1]))
    #     check_digit = 'X' if isbn_without_sep[-1].upper() == 'X' else int(isbn_without_sep[-1])
    #     if check_sum % 11 != 0 or check_digit != check_sum % 11:
    #         raise ValueError('Invalid ISBN-10')
    #
    # # If the input is ISBN-13, calculate the check digit
    # if len(isbn_without_sep) == 13:
    #     check_sum = sum(int(digit) * (3 if i % 2 == 0 else 1) for i, digit in enumerate(isbn_without_sep[:-1]))
    #     check_digit = (10 - (check_sum % 10)) % 10
    #     if int(isbn_without_sep[-1]) != check_digit:
    #         raise ValueError('Invalid ISBN-13')

    return True
