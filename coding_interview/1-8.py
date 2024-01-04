from typing import List
import copy 

def zero_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    Write an algorithm such that if an element in an MxN matrix is 0, its entire
    row and column are set to 0.
    """
    col_size = len(matrix[0]) # 열 크기
    row_size = len(matrix)    # 행 크기
    new_matrix = copy.deepcopy(matrix)

    for i in range(row_size):
        for j in range(col_size):
            if matrix[i][j] == 0:
                # i = 0, j = 4
                for k in range(row_size): # 4
                    new_matrix[k][j] = 0
                for l in range(col_size):
                    new_matrix[i][l] = 0
    return new_matrix

def zero_matrix2(matrix: List[List[int]]) -> List[List[int]]:
    col_size = len(matrix[0]) # 열 크기
    row_size = len(matrix)    # 행 크기

    # 0으로 변경할 행과 열을 저장하는 변수 초기화
    change_row = []
    change_col = []
    for i in range(row_size):
        for j in range(col_size):
            if matrix[i][j] == 0:
                change_row.append(i)
                change_col.append(j)

    change_row = list(set(change_row))
    change_col = list(set(change_col))
    for elem in change_row:
        for i in range(col_size):
            matrix[elem][i] = 0
    for elem in change_col:
        for i in range(row_size):
            matrix[i][elem] = 0

    return matrix

if __name__ == '__main__':
    # Write your test cases here
    matrix = [ [1, 2, 3, 5, 0],
               [4, 5, 6, 1, 2],
               [0, 5, 3, 1, 2],
               [3, 2, 0, 2, 9] ]
    result = [ [0, 0, 0, 0, 0],
               [0, 5, 0, 1, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0] ]

    assert zero_matrix(matrix) == result
    assert zero_matrix2(matrix) == result
