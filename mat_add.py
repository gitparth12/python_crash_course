def add(a, b):
    # check if they are incompatible
    if len(a) != len(b):
        return None
    
    c = []
    # loop through rows 
    for row_i in range(len(a)):
        # get rows from both matrices
        row_a = a[row_i]
        row_b = b[row_i]
        # create a new variable to store result
        result_row = []
        # loop through the columns in that row
        for col_j in range(len(row_a)):
            # add column entry for that row
            result_row.append(row_a[col_j] + row_b[col_j])
        # add row to the result matrix
        c.append(result_row)
    return c


def print_mat(mat):
    for row_i in range(len(mat)):
        row = mat[row_i]
        for col_j in range(len(row)):
            print(mat[row_i][col_j], end=" ")
        print()

a = [[1, 2], [3, 4]]
b = [[1, 0], [0, 1]]

c = add(a, b)
print_mat(c)
