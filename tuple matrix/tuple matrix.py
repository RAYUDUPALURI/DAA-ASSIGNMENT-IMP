def row_wise_addition(matrix):
    num_rows = len(matrix)
    if num_rows == 0:
        print("Matrix is empty.")
        return None
    
    num_cols = len(matrix[0])
    result = [0] * num_cols
    
    for row in matrix:
        if len(row) != num_cols:
            print("Matrix dimensions do not match.")
            return None
        result = tuple(map(sum, zip(result, row)))
    
    return result

matrix = [
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
]

result = row_wise_addition(matrix)
if result:
    print("Row-wise Addition Result:")
    print(result)
