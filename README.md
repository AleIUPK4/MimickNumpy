# Numpy Clone (Final Project)
This Python project provides a simple implementation of a matrix class (Mat) and its subclasses (MatZeros, MatOnes, MatRandom). The goal is to mimic basic matrix operations similar to NumPy but without using NumPy.

Features:
- Matrix Operations: The Mat class supports basic matrix operations, including addition, subtraction, element-wise multiplication, element-wise division, and matrix multiplication.
- Matrix Initialization: The project includes specialized subclasses for creating matrices filled with zeros (MatZeros), ones (MatOnes), and random values (MatRandom).
- Matrix Transpose: The Mat class supports calculating the transpose of a matrix.
- Matrix Determinant and Inverse: Basic implementations for 2x2 matrices are provided for determinant and inverse calculations.

## Usage
```
# Example usage of Mat, MatZeros, MatOnes, and MatRandom

# Creating instances of MatZeros, MatOnes, and MatRandom
mat_zeros = MatZeros((3, 3))
mat_ones = MatOnes((3, 3))
mat_random = MatRandom((3, 3))

# Performing operations on the matrices
result_add = mat_zeros + mat_ones
result_mul = mat_ones * mat_random
result_transpose = mat_random.transpose()

# Printing the results
print("MatZeros + MatOnes:")
print(result_add)

print("\nMatOnes * MatRandom:")
print(result_mul)

print("\nTranspose of MatRandom:")
print(result_transpose)
```

## Requirements
- Python 3.x

## Installation
Clone the repository:

```
git clone https://github.com/your-username/your-repository.git
```
Navigate to the project directory:
```
cd your-repository
```
Run the examples or integrate the Mat class into your own project.
