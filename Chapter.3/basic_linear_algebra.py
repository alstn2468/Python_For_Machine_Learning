def vector_size_check(*vector_variables) :
    return all(len(vector_variables[0]) == x
                for x in [len(vector) for vector in vector_variables[1:]])

def vector_addition(*vector_variables) :
    if vector_size_check(*vector_variables) == False :
        raise ArithmeticError

    return [sum(elements) for elements in zip(*vector_variables)]

def vector_subtraction(*vector_variables) :
    if vector_size_check(*vector_variables) == False :
        raise ArithmeticError

    return [elements[0] * 2 - sum(elements) for elements in zip(*vector_variables)]

def scalar_vector_product(alpha, vector_variable) :
    return [alpha * element for element in vector_variable]

def matrix_size_check(*matrix_variables) :
    return all([len(set(len(matrix[0]) for matrix in matrix_variables)) == 1]) and all([len(matrix_variables[0]) == len(matrix) for matrix in matrix_variables])

def is_matrix_equal(*matrix_variables) :
    return all([all([len(set(row)) == 1 for row in zip(*matrix)])
                for matrix in zip(*matrix_variables)])

def matrix_addition(*matrix_variables) :
    if matrix_size_check(*matrix_variables) == False :
        raise ArithmeticError

    return [[sum(row) for row in zip(*matrix)] for matrix in zip(*matrix_variables)]

def matrix_subtraction(*matrix_variables) :
    if matrix_size_check(*matrix_variables) == False :
        raise ArithmeticError

    return [[row[0] * 2 - sum(row) for row in zip(*matrix)]
                for matrix in zip(*matrix_variables)]

def matrix_transpose(matrix_variable) :
    return [[element for element in row] for row in zip(*matrix_variable)]

def scalar_matrix_product(alpha, matrix_variable) :
    return [scalar_vector_product(alpha, row) for row in matrix_variable]

def is_product_availability_matrix(matrix_a, matrix_b) :
    return len([column_vector for column_vector in zip(*matrix_a)]) == len(matrix_b)

def matrix_product(matrix_a, matrix_b) :
    if is_product_availability_matrix(matrix_a, matrix_b) == False :
        raise ArithmeticError

    return [[sum(a * b for a, b in zip(row_a, column_b))
             for column_b in zip(*matrix_b)] for row_a in matrix_a]


if __name__ == '__main__' :

    # vector_size_check test
    print('-- vector_size_check test --')
    print(vector_size_check([1,2,3], [2,3,4], [5,6,7])) # Expected value: True
    print(vector_size_check([1, 3], [2,4], [6,7]))      # Expected value: True
    print(vector_size_check([1, 3, 4], [4], [6,7]))     # Expected value: False

    # vector_addition test
    print('-- vector_addition test -- ')
    print(vector_addition([1, 3], [2, 4], [6, 7]))  # Expected value: [9, 14]
    print(vector_addition([1, 5], [10, 4], [4, 7])) # Expected value: [15, 16]
    # print(vector_addition([1, 3, 4], [4], [6,7])) # Expected value: ArithmeticError

    # vector_subtraction test
    print('-- vector_subtraction test -- ')
    print(vector_subtraction([1, 3], [2, 4]))          # Expected value: [-1, -1]
    print(vector_subtraction([1, 5], [10, 4], [4, 7])) # Expected value: [-13, -6]

    # scalar_vector_product test
    print('-- scalar_vector_product test -- ')
    print(scalar_vector_product(5,[1,2,3])) # Expected value: [5, 10, 15]
    print(scalar_vector_product(3,[2,2]))   # Expected value: [6, 6]
    print(scalar_vector_product(4,[1]))     # Expected value: [4]

    # matrix_size_check test
    matrix_x = [[2, 2], [2, 2], [2, 2]]
    matrix_y = [[2, 5], [2, 1]]
    matrix_z = [[2, 4], [5, 3]]
    matrix_w = [[2, 5], [1, 1], [2, 2]]

    print('-- matrix_size_check test -- ')
    print(matrix_size_check(matrix_x, matrix_y, matrix_z)) # Expected value: False
    print(matrix_size_check(matrix_y, matrix_z))           # Expected value: True
    print(matrix_size_check(matrix_x, matrix_w))           # Expected value: True

    # is_matrix_equal test
    matrix_x = [[2, 2], [2, 2]]
    matrix_y = [[2, 5], [2, 1]]

    print('-- is_matrix_equal test -- ')
    print(is_matrix_equal(matrix_x, matrix_y, matrix_y, matrix_y)) # Expected value: False
    print(is_matrix_equal(matrix_x, matrix_x))                     # Expected value: True

    # matrix_addition test
    matrix_x = [[2, 2], [2, 2]]
    matrix_y = [[2, 5], [2, 1]]
    matrix_z = [[2, 4], [5, 3]]

    print('-- matrix_addition test -- ')
    print(matrix_addition(matrix_x, matrix_y))           # Expected value: [[4, 7], [4, 3]]
    print(matrix_addition(matrix_x, matrix_y, matrix_z)) # Expected value: [[6, 11], [9, 6]]

    # matrix_subtraction test
    matrix_x = [[2, 2], [2, 2]]
    matrix_y = [[2, 5], [2, 1]]
    matrix_z = [[2, 4], [5, 3]]

    print('-- matrix_subtraction test -- ')
    print(matrix_subtraction(matrix_x, matrix_y))           # Expected value: [[0, -3], [0, 1]]
    print(matrix_subtraction(matrix_x, matrix_y, matrix_z)) # Expected value: [[-2, -7], [-5, -2]]

    # matrix_transpose test
    matrix_w = [[2, 5], [1, 1], [2, 2]]

    print('-- matrix_transpose test -- ')
    print(matrix_transpose(matrix_w)) # Expected value: [[2, 1, 2], [5, 1, 2]]

    # scalar_matrix_product test
    matrix_x = [[2, 2], [2, 2], [2, 2]]
    matrix_y = [[2, 5], [2, 1]]
    matrix_z = [[2, 4], [5, 3]]
    matrix_w = [[2, 5], [1, 1], [2, 2]]

    print('-- scalar_matrix_product test -- ')
    print(scalar_matrix_product(3, matrix_x)) # Expected value: [[6, 6], [6, 6], [6, 6]]
    print(scalar_matrix_product(2, matrix_y)) # Expected value: [[4, 10], [4, 2]]
    print(scalar_matrix_product(4, matrix_z)) # Expected value: [[8, 16], [20, 12]]
    print(scalar_matrix_product(3, matrix_w)) # Expected value: [[6, 15], [3, 3], [6, 6]]

    # is_product_availability_matrix test
    matrix_x = [[2, 5], [1, 1]]
    matrix_y = [[1, 1, 2], [2, 1, 1]]
    matrix_z = [[2, 4], [5, 3], [1, 3]]

    print('-- is_product_availability_matrix test -- ')
    print(is_product_availability_matrix(matrix_y, matrix_z)) # Expected value: True
    print(is_product_availability_matrix(matrix_z, matrix_x)) # Expected value: True
    print(is_product_availability_matrix(matrix_z, matrix_w)) # Expected value: False
    print(is_product_availability_matrix(matrix_x, matrix_x)) # Expected value: True

    # matrix_product test
    matrix_x = [[2, 5], [1, 1]]
    matrix_y = [[1, 1, 2], [2, 1, 1]]
    matrix_z = [[2, 4], [5, 3], [1, 3]]

    print('-- matrix_product test -- ')
    print(matrix_product(matrix_y, matrix_z)) # Expected value: [[9, 13], [10, 14]]
    print(matrix_product(matrix_z, matrix_x)) # Expected value: [[8, 14], [13, 28], [5, 8]]
    print(matrix_product(matrix_x, matrix_x)) # Expected value: [[9, 15], [3, 6]]
    # print(matrix_product(matrix_z, matrix_w)) # Expected value: False
