# numpy_lab.py

import numpy as np

def n_size_ndarray_creation(n, dtype = np.int) :
    return np.array(range(n ** 2),
                    dtype = dtype).reshape(n, n)

def zero_or_one_or_empty_ndarray(shape, type = 0, dtype = np.int) :
    if type == 0 :
        return np.zeros(shpae = shape, dtype = dtype)

    if type == 1 :
        return np.ones(shape = shape, dtype = dtype)

    if type == 99 :
        return np.empty(shape = shape, dtype = dtype)

def change_shape_of_ndarray(X, n_row) :
    return X.flatten() if n_row == 1 else X.reshape(n_row, -1)

def concat_ndarray(X_1, X_2, axis) :
    try :
        if X_1.ndim == 1 :
            X_1 = X_1.reshape(1, -1)

        if X_2.ndim == 1 :
            X_2 = X_2.reshape(1, -1)

        return np.concatenate((X_1, X_2), axis = axis)

    except ValueError as e :
        return False


def normalize_ndarray(X, axis = 99, dtype = np.float32) :
    X = X.astype(np.float32)

    n_row, n_column = X.shape

    if axis == 99 :
        x_mean = np.mean(X)
        x_std = np.std(X)
        Z = (X - x_mean) / x_std

    if axis == 0 :
        x_mean = np.mean(X, 0).reshape(1, -1)
        x_std = np.std(X, 0).reshape(1, -1)
        Z = (X - x_mean) / x_std

    if axis == 1 :
        x_mean = np.mean(X, 1).reshape(n_row, -1)
        x_std = np.std(X, 1).reshape(n_row, -1)
        Z = (X - x_mean) / x_std

    return Z

def save_ndarray(X, filename = "test.npy") :
    np.save(filename, X)

def boolean_index(X, condition) :
    condition = eval(str('X') + condition)

    return np.where(condition)

def find_nearest_value(X, target_value) :
    return X[np.argmin(np.abs(X - target_value))]

def get_n_largest_values(X, n) :
    return X[np.argsort(X[::-1])[:n]]


if __name__ == '__main__' :

    # zero_or_one_or_empty_ndarray test
    print('- zero_or_one_or_empty_ndarray test -')
    print(zero_or_one_or_empty_ndarray(shape = (2, 2), type = 1))
    print(zero_or_one_or_empty_ndarray(shape = (3, 3), type = 99))
    '''
    [[1 1]
    [1 1]]
    [[ 1152921504606846976  1152921504606846976 -9223372036854775794]
    [                   0           4294967296                    0]
    [                   0                    0       35596688949248]]
    '''


    # change_shape_of_ndarray test
    X = np.ones((32, 32), dtype = np.int)

    print('- change_shape_of_ndarray test -')
    print(change_shape_of_ndarray(X, 1))
    print(change_shape_of_ndarray(X, 512))
    '''
    [1 1 1 ..., 1 1 1]
    [[1 1]
     [1 1]
     [1 1]
     ...,
     [1 1]
     [1 1]
     [1 1]]
    '''


    # concat_ndarray test
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6]])

    print('- concat_ndarray test -')
    print(concat_ndarray(a, b, 0))
    print(concat_ndarray(a, b, 1))

    a = np.array([1, 2])
    b = np.array([5, 6, 7])

    print(concat_ndarray(a, b, 1))
    print(concat_ndarray(a, b, 0))
    '''
    [[1 2]
     [3 4]
     [5 6]]
    False
    [[1 2 5 6 7]]
    False
    '''


    # normalize_ndarray test
    X = np.arange(12, dtype = np.float32).reshape(6, 2)

    print('- normalize_ndarray test -')
    print(normalize_ndarray(X))
    print(normalize_ndarray(X, 1))
    print(normalize_ndarray(X, 0))
    '''
    [[-1.59325504 -1.3035723 ]
     [-1.01388955 -0.72420681]
     [-0.43452409 -0.14484136]
     [ 0.14484136  0.43452409]
     [ 0.72420681  1.01388955]
     [ 1.3035723   1.59325504]]
     [[-1.  1.]
     [-1.  1.]
     [-1.  1.]
     [-1.  1.]
     [-1.  1.]
     [-1.  1.]]
     [[-1.46385002 -1.46385002]
     [-0.87831002 -0.87831002]
     [-0.29277    -0.29277   ]
     [ 0.29277     0.29277   ]
     [ 0.87831002  0.87831002]
     [ 1.46385002  1.46385002]]
    '''


    # save_ndarray test
    X = np.arange(32, dtype = np.float32).reshape(4, -1)
    filename = "test.npy"
    save_ndarray(X, filename)


    # boolean_index test

    print('- boolean_index test -')
    X = np.arange(32, dtype = np.float32).reshape(4, -1)
    print(boolean_index(X, '== 3'))

    X = np.arange(32, dtype = np.float32)
    print(boolean_index(X, "> 6"))
    '''
    (array([0]), array([3]))
    (array([ 7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
           24, 25, 26, 27, 28, 29, 30, 31]),)
    '''


    # find_nearest_value test
    X = np.random.uniform(0, 1, 100)
    target_value = 0.3

    print('- find_nearest_value test -')
    print(find_nearest_value(X, target_value))
    '''
    0.288636002593
    '''

    # get_n_largest_values test
    X = np.random.uniform(0, 1, 100)

    print('- get_n_largest_values test -')
    print(get_n_largest_values(X, 3))
    print(get_n_largest_values(X, 5))
    '''
    [ 0.5953649   0.88120884  0.14864755]
    [ 0.5953649   0.88120884  0.14864755  0.31801284  0.58373682]
    '''
