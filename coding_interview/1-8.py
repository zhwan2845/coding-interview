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
    pass # HW 1/4

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
