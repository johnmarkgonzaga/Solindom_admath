import numpy as np

def determinant_matrices(matrix_A, matrix_B):
    np_matA = np.array(matrix_A, dtype=float)
    np_matB = np.array(matrix_B, dtype=float)

    determinant_matrix_A = np.linalg.det(np_matA) #execute and value holder for A
    determinant_matrix_B = np.linalg.det(np_matB) #execute and value holder for B
    return determinant_matrix_A, determinant_matrix_B