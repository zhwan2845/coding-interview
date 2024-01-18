from typing import List

def rotate_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    Given an image represented by an NxN matrix, where each pixel in the image
    is 4 bytes, write a method to rotate the image by 90 degrees. Can you do
    this in place?
    """
    n = len(matrix[0])
    new_matrix = []
    for i in range(n):
        tmp = []
        for j in range(n):
            tmp.append(n)
        new_matrix.append(tmp)

    for i in range(n):
        for j in range(n):
            new_matrix[j][n - i - 1] = matrix[i][j]
    return new_matrix

def rotate_matrix_180(matrix: List[List[int]]) -> List[List[int]]:
    n = len(matrix[0])
    new_matrix = []
    for i in range(n):
        array = []
        for j in range(n):
            array.append(0)
        new_matrix.append(array)
        
    for i in range(n):
        for j in range(n):
            new_matrix[n - i - 1][n - j - 1] = matrix[i][j]
    return new_matrix

def rotate_matrix_270(matrix: List[List[int]]) -> List[List[int]]:
    n = len(matrix[0])
    new_matrix = []
    for i in range(n):
        tmp = []
        for j in range(n):
            tmp.append(n)
        new_matrix.append(tmp)

    for i in range(n):
        for j in range(n):
            new_matrix[n - j - 1][i] = matrix[i][j]
    return new_matrix

if __name__ == '__main__':
    # Write your test cases here
    assert rotate_matrix([[1,2,3], [4,5,6], [7,8,9]]) == [[7,4,1], [8,5,2], [9,6,3]]
    assert rotate_matrix_180([[1,2,3], [4,5,6], [7,8,9]]) == [[9,8,7], [6,5,4], [3,2,1]]
    assert rotate_matrix_270([[1,2,3], [4,5,6], [7,8,9]]) == [[3,6,9], [2,5,8], [1,4,7]] 
