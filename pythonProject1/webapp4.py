def BinToDecimal(binary):

    def num_binary(number):
        return all(digit in '01' for digit in str(number))

    def convert_bin_to_dec(bin_number):
        decimal = 0
        power = len(bin_number) - 1
        for digit in bin_number:
            decimal += int(digit) * (2 ** power)
            power -= 1
        return decimal

    if num_binary(binary):
        binary_number = str(binary)
        if binary_number.startswith("0b"):
            binary_number = binary_number[2:]
        decimal_number = convert_bin_to_dec(binary_number)
        return decimal_number
    else:
        st.error("Invalid Binary Number")

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

