import random

class Mat:
    def __init__(self, matrix):
        self.matrix = matrix
        self.shape = self._shape()
        if isinstance(matrix[0], list):
            col_length = len(matrix[0])
            for i, row in enumerate(matrix):
                assert all(isinstance(r, (float, int)) for r in row), "Mat can only be 2d"

    def __str__(self):
        max_len = self._max_element_length() + 4

        pretty_print = ""
        for row in self.matrix:
            if not isinstance(row, list):
                pretty_print += str(f"{row:.2f}") + " "
            else:
                pretty_print += "  "
                for col in row:
                    pretty_print += str(f"{col:.2f}").ljust(max_len) + " "
                pretty_print += "\n"
        
        if not isinstance(row, list):
            pretty_print = "Matrix(\n  "+pretty_print+"\n)"
        else:
            pretty_print = "Matrix(\n"+pretty_print+")"

        return pretty_print
    
    def _shape(self):
        row = len(self.matrix)
        column = len(self.matrix[0])
        return [row, column]

    def transpose(self):
        new_matrix = [[self.matrix[x][y] for x in range(self.shape[0])] for y in range(self.shape[1])]
        return Mat(new_matrix)

    def determinant(self):
        # Implement matrix determinant calculation (for 2x2 matrix)
        if self.shape[0] != self.shape[1] or self.shape[0] != 2:
            raise ValueError("Determinant is only defined for 2x2 matrices.")
        return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]

    def inverse(self):
        # Implement matrix inverse calculation (for 2x2 matrix)
        det = self.determinant()
        if det == 0:
            raise ValueError("Matrix is not invertible.")
        inv_det = 1 / det
        new_matrix = [
            [self.matrix[1][1] * inv_det, -self.matrix[0][1] * inv_det],
            [-self.matrix[1][0] * inv_det, self.matrix[0][0] * inv_det]
        ]
        return Mat(new_matrix)

    def _max_element_length(self):
        return max(
            max([len(str(round(col, 2))) for col in row]) if isinstance(row, list) else len(str(round(row, 2)))
            for row in self.matrix
        )

    def __add__(self, other):
        return self._elementwise_operation(other, lambda x, y: x + y)

    def __sub__(self, other):
        return self._elementwise_operation(other, lambda x, y: x - y)

    def __mul__(self, other):
        return self._elementwise_operation(other, lambda x, y: x * y)

    def __truediv__(self, other):
        return self._elementwise_operation(other, lambda x, y: x / y)

    def __floordiv__(self, other):
        return self._elementwise_operation(other, lambda x, y: x // y)

    def __matmul__(self, other):
        if self.shape[1] != other.shape[0]:
            raise ValueError("Incompatible matrix dimensions for matrix multiplication.")
    
        new_matrix = [
            [sum(self.matrix[x][k] * other.matrix[k][y] for k in range(self.shape[1])) for y in range(other.shape[1])]
            for x in range(self.shape[0])
            ]
        return Mat(new_matrix)


    def _elementwise_operation(self, other, operation):
        if self.shape != other.shape:
            raise ValueError("Both matrices must have the same shape.")
        
        new_matrix = [
            [operation(self.matrix[x][y], other.matrix[x][y]) for y in range(self.shape[1])]
            for x in range(self.shape[0])
        ]
        return Mat(new_matrix)
    
    def flatten(self):
        return [element for row in self.matrix for element in (row if isinstance(row, list) else [row])]


class MatZeros(Mat):
    def __init__(self, shape):
        matrix_zeros = [[0] * shape[1] for _ in range(shape[0])]
        super().__init__(matrix_zeros)

class MatOnes(Mat):
    def __init__(self, shape):
        matrix_ones = [[1] * shape[1] for _ in range(shape[0])]
        super().__init__(matrix_ones)

class MatRandom(Mat):
    def __init__(self, shape):
        matrix_random = [[random.randrange(10, 100) for _ in range(shape[1])] for _ in range(shape[0])]
        super().__init__(matrix_random)
