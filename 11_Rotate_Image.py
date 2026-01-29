class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        matrix_b = []

        for i in range(n):
            row = []
            for j in range(n):
                row.append(matrix[n - 1 - j][i])
            matrix_b.append(row)

        matrix[:] = matrix_b


matrix = eval(input())

Solution().rotate(matrix)

print(matrix)
