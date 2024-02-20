from typing import List


def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    length = len(matrix)
    idx = 0

    while length > idx:
        for x in range(idx, length):
            matrix[x], matrix[end]

        idx += 1
        
    print(matrix)
    
    
rotate([[1,2,3],[4,5,6],[7,8,9]])
    