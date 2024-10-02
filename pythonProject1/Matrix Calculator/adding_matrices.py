def adding_matrices(matrix_A, matrix_B):
    row = len(matrix_A)
    column = len(matrix_A[0])
    sum_matrix = []
    for i in range(row):
        temporary_list = []
        for j in range(column):
            value = matrix_A[i][j] + matrix_B[i][j]
            temporary_list.append(value)
        sum_matrix.append(temporary_list)
    return sum_matrix