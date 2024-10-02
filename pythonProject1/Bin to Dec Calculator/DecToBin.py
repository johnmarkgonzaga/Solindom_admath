def DecToBin(number):
    if number == 0:
        return "0"

    # If negative numbers
    is_negative = False
    if number < 0:
        is_negative = True
        number = abs(number)

    binary_digits = []
    while number > 0:
        remainder = number % 2
        binary_digits.append(str(remainder))
        number //= 2

    binary_digits.reverse()
    binary_number = "".join(binary_digits)

    if is_negative:
        return "-" + binary_number
    else:
        return binary_number