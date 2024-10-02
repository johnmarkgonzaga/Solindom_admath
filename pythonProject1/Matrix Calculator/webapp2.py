import streamlit as st
import adding_matrices as am
import multiplying_matrices as ma
import Transpose_matrices as tm
import Inverse_matrices as im
import determinant_matrices as dm
import numpy as np
st.set_page_config(page_title="MATRIX CALCULATOR", page_icon="🎓", layout="centered")
st.markdown(
    """
    <style>
    .stApp{
        background-color :  #D2B05B;

    }
    </style>
    """,
    unsafe_allow_html=True)
with st.container():
    st.markdown(
        "<h1 style='text-align: center; font-size: 80px; font-weight: bold; color: green;'>MATRIX CALCULATOR®️</h1>",
        unsafe_allow_html=True)
with st.container():
    st.write("---")
st.sidebar.title('Matrix Calculator')
choices = st.sidebar.selectbox('Select Option', ('Home', 'MATRIX CALCULATOR', 'About app'))

if choices == 'Home':
    st.markdown("""
                <h1 style="font-size: 40px; font-family: 'Arial, serif'; text-align: center">
                Welcome to my Webapp!
                </h1>
                <p style='text-align: center; font-size: 18px;'>A Calculator app for matrices.</p>
            """, unsafe_allow_html=True)
elif choices == 'MATRIX CALCULATOR':
    st.write('Matrix Calculator')

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
            <h1 style="font-size: 24px; font-family: 'Arial, sans-serif'; text-align: center ; color: blue">
            Enter the size of the matrices:
            </h1>
        """, unsafe_allow_html=True)
    with col2:
        row = st.number_input("ROW:", min_value=1, max_value=5, key='row')
    with col3:
        column = st.number_input("COLUMN:", min_value=1, max_value=5, key='column')

    col4, col5 = st.columns(2)
    with col4:
        st.markdown("""
                <h1 style="font-size: 24px; font-family: 'Arial, sans-serif'; color: blue">
                Matrix A
                </h1>
            """, unsafe_allow_html=True)
        for row_index in range(row):
            columns = st.columns(column)
            for col_index, col in enumerate(columns):
                with col:
                    st.text_input("", key=f'Arow{row_index + 1}Acol{col_index + 1}')

    with col5:
        st.markdown("""
                    <h1 style="font-size: 24px; font-family: 'Arial, sans-serif'; color: blue">
                    Matrix B
                    </h1>
                """, unsafe_allow_html=True)
        for row_index in range(row):
            columns = st.columns(column)
            for col_index, col in enumerate(columns):
                with col:
                    st.text_input("", key=f'Brow{row_index + 1}Bcol{col_index + 1}')

    operation = st.selectbox("Choose Operation",["Addition", "Multiplication", "Transpose", "Inverse", "Determinant"])
    matA = []
    matB = []
    for i in range(row):
        rowSum = []
        for j in range(column):
            for value in st.session_state:
                if value == f"Arow{i + 1}Acol{j + 1}":
                    rowSum.append(st.session_state[value])
        matA.append(rowSum)
    print(matA)
    for i in range(row):
        rowSum = []
        for j in range(column):
            for value in st.session_state:
                if value == f"Brow{i + 1}Bcol{j + 1}":
                    rowSum.append(st.session_state[value])
        matB.append(rowSum)
    print(matB)

    print(st.session_state)


    calculate = st.button("Calculate Matrix", key='calculate_button')
    if calculate:
        if operation == 'Addition of matrices':
            calculating_matrix = am.adding_matrices(matA, matB)
            st.success('Addition calculated successfully!')
            col6, col7, col8 = st.columns(3)
            with col7:
                for row_index in range (row):
                    columns = st.columns(column)
                    for col_index, col in enumerate(columns):
                        with col:
                            st.text_input("", value=calculating_matrix[row_index][col_index], key=f'Rrow{row_index + 1}Rcol{col_index + 1}')

        elif operation == 'Multiplication of matrices':
            calculating_matrix = ma.multiplying_matrices(matA, matB)
            st.success('Multiplication calculated successfully!')
            col6, col7, col8 = st.columns(3)
            with col7:
                for row_index in range(row):
                    columns = st.columns(column)
                    for col_index, col in enumerate(columns):
                        with col:
                            st.text_input("", value=str(calculating_matrix[row_index][col_index]), key=f'Rrow{row_index + 1}Rcol{col_index + 1}')

        elif operation == 'Transpose of matrices':
            calculating_matrix = tm.transpose_matrices(matA, matB)
            st.success('Transposed Matrix calculated successfully!')
            col8, col9 = st.columns(2)
            with col8:
                for row_index in range(len(calculating_matrix)):
                    columns = st.columns(len(calculating_matrix[0]))
                    for col_index, col in enumerate(columns):
                        with col:
                            if row_index < len(calculating_matrix) and col_index < len(calculating_matrix[0]):
                                st.text_input("", value=calculating_matrix[row_index][col_index],
                                              key=f'Rrow{row_index + 5}Rcol{col_index + 5}', max_chars=2)
                            else:
                                st.text_input("", value="Index out of range",
                                              key=f'Rrow{row_index + 5}Rcol{col_index + 5}', max_chars=2)

        elif operation == 'Inverse of matrices':
            calculating_matrices = im.inverse_matrices(matA, matB)
            if calculating_matrices is not None and len(calculating_matrices) == 2 and all(matrix is not None for matrix in calculating_matrices):
                calculating_matrixA, calculating_matrixB = calculating_matrices
                st.success('Inverse Matrix calculated successfully!')
                col6, col7 = st.columns(2)
                with col6:
                    for row_index in range(len(calculating_matrixA)):
                        for col_index in range(len(calculating_matrixA[row_index])):
                            st.text_input("", value=str(calculating_matrixA[row_index][col_index]),
                                          key=f'A_{row_index + 1}Acol{col_index + 1}')
                with col7:
                    for row_index in range(len(calculating_matrixB)):
                        for col_index in range(len(calculating_matrixB[row_index])):
                            st.text_input("", value=str(calculating_matrixB[row_index][col_index]),
                                          key=f'B_{row_index + 1}Bcol{col_index + 1}')
            else:
                st.error("Ensure matrices are invertible.")

        elif operation == "Determinant of matrices":
            calculating_matrices = dm.determinant_matrix(matA, matB)
            if calculating_matrices is not None and len(calculating_matrices) == 2 and all(matrix is not None for matrix in calculating_matrices):
                determinant_A, determinant_B = calculating_matrices
                st.success('Determinant Matrix calculated successfully!')
                st.write(f'Determinant of Matrix A: {determinant_A}')
                st.write(f'Determinant of Matrix B: {determinant_B}')
            else:
                st.error("Error: Determinants calculation failed.")
else:
    st.sidebar.info("This app allows users to input the dimensions and values to perform addition, multiplication,"
                    " inverse, transpose, and determinant operations on two matrices. The result is displayed"
                    " accordingly.")
    st.markdown("""
        ### You can contact us via ff:
        - Email: johnmarksolindom@gmail.com
        - Phone: 09518235460

        ### Connect with us via Facebook
        - https://www.facebook.com/johnmarksolindom


        For more inquiries, Please visit us on DME . Arigatou!!!.
        """)
