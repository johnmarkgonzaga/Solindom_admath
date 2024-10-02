import streamlit as st
import BinToDec as bd
import time
def decimal_to_binary(decimal):
    decimal = int(decimal)
    binary = bin(decimal).replace("0b", "")
    return binary
st.title('Binary and Decimal Converter')
st.markdown("<h2 style='text-align: center; color: orange;'>Vice Versa</h2>",
unsafe_allow_html=True)
st.subheader('By: John Mark G. Solindom')
st.markdown("---")
st.markdown("Welcome to the Binary and Decimal Converter App!:wave:")
st.sidebar.title("About")
st.sidebar.info(" This app converts decimal to their equivalent binary representation or vice versa. ")

("A Binary and Decimal Converter web app is a tool that allows user to convert numbers between binary"
                "(base-2) and decimal (base-10) representations. Users can input a number in either binary or decimal"
                "format, and the web app will convert it to other base.")
conversion_type = st.selectbox('Choose conversion type:', ('Binary to Decimal', 'Decimal to Binary'))

if conversion_type == 'Binary to Decimal':
    binary_input = st.text_input('Enter a binary number:', value='', max_chars=None, key="binary_number", type='default')
    if st.button('Convert to Decimal'):
        if all([bit in ['0', '1'] for bit in binary_input]):
            decimal_output =bd.BinToDecimal(int(binary_input))
            st.write('Decimal:', decimal_output)
            with st.spinner("wait for it..."):
                time.sleep(1)
        else:
            st.write('Please enter a valid binary number.')
else:
    decimal_input = st.text_input('Enter a decimal number:', value='', max_chars=None, key=None, type='default')
    if st.button('Convert to Binary'):
        if decimal_input.isdigit():
            binary_output = decimal_to_binary(decimal_input)
            st.write('Binary:', binary_output)
            with st.spinner("wait for it..."):
                time.sleep(1)
        else:
            st.write('Please enter a valid decimal number.')