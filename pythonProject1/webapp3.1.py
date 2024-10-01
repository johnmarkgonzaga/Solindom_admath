import streamlit as st
import numpy as np
from LE_solver import lu_decomposition
# https://web.facebook.com/photo/?fbid=520426773461731&set=pcb.520427796794962
#https://c4.wallpaperflare.com/wallpaper/569/152/9/minimalism-geometric-landscape-wallpaper-preview.jpg
background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://c4.wallpaperflare.com/wallpaper/569/152/9/minimalism-geometric-landscape-wallpaper-preview.jpg");
    background-size: 100vw 100vh;
    background-position: center;  
    background-repeat: no repeat;
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)

def solve_lu_decomposition(L, U, B):
    n = len(B)
    y = np.zeros(n)
    x = np.zeros(n)

    # Solve Ly = B
    for i in range(n):
        y[i] = B[i] - np.dot(L[i, :i], y[:i])

    # Solve Ux = y
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]

    return x

st.sidebar.title('LINEAR EQUATION CALCULATOR')
choices = st.sidebar.selectbox('Select Option', ('Home', 'Linear Equations Calculator', 'About app'))

if choices == 'Home':
    st.markdown("""
                <h1 style='text-align: center; font-size: 60px; font: Arial; color: azure;'> 
                LINEAR EQUATIONS CALCULATOR
                </h1>
                <p style='text-align: center; font-size: 18px;'>A Calculator app for linear equations.</p>
            """, unsafe_allow_html=True)
elif choices == 'Linear Equations Calculator':

    def main():
        st.markdown(
            "<h1 style='text-align: center; font-size: 43px; font-weight: bold; color: brown ;'>LINEAR EQUATIONS CALCULATOR🔍</h1>",
            unsafe_allow_html=True)
        st.write("---")
        st.markdown("""
                            <h1 style="font-size: 24px; font-family: 'Arial, sans-serif'; text-align: center; color: blue">
                            Input number of Linear Equations:
                            </h1>
                        """, unsafe_allow_html=True)
        num_equations = st.number_input("", min_value=2, max_value=5)

        A = np.zeros((num_equations, num_equations))
        B = np.zeros(num_equations)

        st.markdown(f"<h2 style='color: red; font-size: 25px;'> Enter Coefficients in each Equations:",
                    unsafe_allow_html=True)
        equation_columns = st.columns(num_equations)
        for i in range(num_equations):
            with equation_columns[i]:
                st.markdown(f"<h2 style='color: orange; font-size: 20px;'>EQUATION {i + 1}:</h2>",
                            unsafe_allow_html=True)
                for j in range(num_equations):
                    coeff_title = f"Coefficient {i + 1},{j + 1}"
                    A[i, j] = st.number_input(coeff_title, format="%f", key=f"A_{i}_{j}")

        st.markdown(f"<h2 style='color: red; font-size: 25px;'> Enter Constants:",
                    unsafe_allow_html=True)
       for i in range(num_equations):
            const_title = f"Constant {i + 1}"
            B[i] = st.number_input(const_title, format="%f", key=f"b_{i}")

        if st.button("Calculate"):
            L, U = lu_decomposition(A)
            roots = solve_lu_decomposition(L, U, B)

            st.markdown("""
                                    <h1 style="font-size: 25px; font-family: 'Arial, sans-serif'; text-align: center; color: blue">
                                    THE STEP-BY-STEP SOLUTION:
                                    </h1>
                                    """, unsafe_allow_html=True)

            st.markdown("### LOWER TRIANGULAR MATRIX (L):")
            st.write(np.round(L, 2))

            st.markdown("### UPPER TRIANGULAR MATRIX (U):")
            st.write(np.round(U, 2))

            st.markdown("### Solution:")
            for i, root in enumerate(roots):
                st.write(f"X_{i + 1} = {root}")


    if __name__ == "__main__":
        main()
else:
    st.sidebar.info("This app first performs LU decomposition of the equation 1, then solves the linear equations using"
                    " the LU factors. You can replace the coefficients in each equations with your own values to solve"
                    " different linear equations.")
    st.markdown("""
        ### You can contact us via ff:
        - Email: johnmarksolindom@gmail.com
        - Phone: 09518235460

        ### Connect with us via Facebook
        - https://www.facebook.com/johnmarksolindom


        For more inquiries, Please visit us on DME . Arigatou!!!.
        """)
