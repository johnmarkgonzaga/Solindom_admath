import numpy as np
import streamlit as st
def inversematrices(matA, matB):
    try:
        np_matA = np.array(matA, dtype=float)
        np_matB = np.array(matB, dtype=float)

        inv_matA = np.linalg.inv(np_matA) # Calculate the inverse of matA
        inv_matB = np.linalg.inv(np_matB) # Calculate the inverse of matB

        return inv_matA, inv_matB
    except np.linalg.LinAlgError as e:
        st.error("Error: Singular matrix. Cannot invert the matrices.")
        return None, None

#determinant of matrices
import numpy as np
def Determinant_matrices(matA, matB):
    np_matA = np.array(matA, dtype=float)
    np_matB = np.array(matB, dtype=float)

    det_matA = np.linalg.det(np_matA) # Calculate determinant of matA
    det_matB = np.linalg.det(np_matB) # Calculate determinant of matB
    return det_matA, det_matB
