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