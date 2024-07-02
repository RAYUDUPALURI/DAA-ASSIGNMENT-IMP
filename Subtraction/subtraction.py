def add_matrices(A, B):
   
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        print("Matrix dimensions do not match.")
        return None
    
   
    result = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]
    
    
    for i in range(len(A)):
        for j in range(len(A[0])):
            result[i][j] = A[i][j] + B[i][j]
    
    return result

def subtract_matrices(A, B):
    
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        print("Matrix dimensions do not match.")
        return None
    
    
    result = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]
    
   
    for i in range(len(A)):
        for j in range(len(A[0])):
            result[i][j] = A[i][j] - B[i][j]
    
    return result


matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result_add = add_matrices(matrix1, matrix2)
if result_add:
    print("Matrix Addition Result:")
    for row in result_add:
        print(row)

result_subtract = subtract_matrices(matrix1, matrix2)
if result_subtract:
    print("\nMatrix Subtraction Result:")
    for row in result_subtract:
        print(row)
