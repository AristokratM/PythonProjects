from tabulate import tabulate


def zero_matrix(n, m):
    z_matrix = [0] * n
    for i in range(n):
        z_matrix[i] = [0] * m
    return z_matrix


def identity_matrix(n):
    i_matrix = zero_matrix(n, n)
    for i in range(n):
        i_matrix[i][i] = 1
    return i_matrix


def copy_matrix(matrix):
    c_matrix = zero_matrix(len(matrix), len(matrix[0]))
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            c_matrix[i][j] = matrix[i][j]
    return c_matrix


def transposed_matrix(matrix):
    tr_matrix = zero_matrix(len(matrix[0]), len(matrix))
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            tr_matrix[j][i] = matrix[i][j]
    return tr_matrix


def matrix_mul(matrix1, matrix2):
    result_matrix = zero_matrix(len(matrix1), len(matrix2[0]))
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix1[0])):
                # print("i = {} j = {} k = {}".format(i, j, k))
                result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
    return result_matrix


def bin_pow(matrix, n):
    res_matrix = identity_matrix(len(matrix))
    pow_matrix = copy_matrix(matrix)
    while n > 0:
        if n % 2:
            res_matrix = matrix_mul(res_matrix, pow_matrix)
        pow_matrix = matrix_mul(pow_matrix, pow_matrix)
        n = n >> 1
    return res_matrix


def matrix_print(matrix, headers, columns):
    c_matrix = copy_matrix(matrix)
    for i in range(len(matrix)):
        c_matrix[i] = [columns[i]] + matrix[i]
    print(tabulate(c_matrix, headers=headers, tablefmt='orgtbl'))


def main():
    start_state = [
        [1],
        [0],
        [0]
    ]
    start_matrix = [
        [0.7, 0.3, 0],
        [0.5, 0.4, 0.1],
        [0.2, 0.3, 0.5]
    ]
    number_of_days = 3
    headers = ['Sun', 'Rain', 'Fog']

    print("Початкова матриця:")
    matrix_print(start_matrix, headers, headers)
    tr_matrix = transposed_matrix(start_matrix)
    print("Транспонована початкова матриця:")
    matrix_print(tr_matrix, headers, headers)
    res_matrix = bin_pow(tr_matrix, number_of_days)
    print("Матриця через {} днів:".format(number_of_days))
    matrix_print(res_matrix, headers, headers)
    ans_matrix = matrix_mul(res_matrix, start_state)
    print("Відповідь: ")
    matrix_print(transposed_matrix(ans_matrix), headers=headers, columns=['Probability'])
    # matrix_print(transposed_matrix(ans_matrix), headers, ['Probability'])


if __name__ == '__main__':
    main()