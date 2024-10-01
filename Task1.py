class Matrix:
    def __init__(self, matrix: list):
        self.matrix = matrix

    def add(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Size of matrix doesn't match")
        res_matrix = [[0 for i in range(len(self.matrix))] for i in range(len(self.matrix[0]))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                res_matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(res_matrix)

    def subtract(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Size of matrix doesn't match")
        res_matrix = [[0 for i in range(len(self.matrix))] for i in range(len(self.matrix[0]))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                res_matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]
        return Matrix(res_matrix)

    def multiply(self, other):
        if len(self.matrix[0]) != len(other.matrix):
            raise ValueError('The number of cols of first matrix must much the number of rows of the second matrix')
        res_matrix = [[0 for i in range(len(self.matrix))] for i in range(len(self.matrix[0]))]
        for i in range(len(self.matrix)):
            for j in range(len(other.matrix[0])):
                for k in range(len(self.matrix[0])):
                    res_matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return Matrix(res_matrix)

    def transposition(self):
        res_matrix = [[0 for i in range(len(self.matrix))] for i in range(len(self.matrix[0]))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                res_matrix[j][i] = self.matrix[i][j]
        return Matrix(res_matrix)

    def __str__(self):
        image = ''
        for row in self.matrix:
            image += f'{row}\n'
        return image


if __name__ == '__main__':
    matrix1 = Matrix([[1, 5, 3], [4, 8, 6], [7, 1, 9]])
    matrix2 = Matrix([[4, 5, 4], [3, 8, 7], [3, 2, 8]])
    print(matrix1)
    print(matrix2)
    # print(matrix1.transposition())
    # print(matrix1.add(matrix2))
    # print(matrix1.subtract(matrix2))
    print(matrix1.multiply(matrix2))
