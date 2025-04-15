# https://leetcode.com/problems/set-matrix-zeroes/description/
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        col0 = 1  # To track if the first column needs to be zeroed
        rows, cols = len(matrix), len(matrix[0])

        # First pass: use matrix[i][0] and matrix[0][j] as flags
        for i in range(rows):
            if matrix[i][0] == 0:
                col0 = 0  # First column will need to be zeroed
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # Mark the row
                    matrix[0][j] = 0  # Mark the column

        # Second pass: apply zeros based on flags, in reverse to avoid overwriting markers
        for i in range(rows - 1, -1, -1):      # Start from the last row and go up
            for j in range(cols - 1, 0, -1):   # Start from last column and go left, skip j=0
                # If either the row or column is marked, set current cell to 0
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            # After handling columns 1 to n-1, handle the first column separately
            if col0 == 0:
                matrix[i][0] = 0
