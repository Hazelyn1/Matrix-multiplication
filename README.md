# Matrix-multiplication
This program was written in Python 3.8 in the IDE PyCharm, version 2021.2. This program can also be run on command line given that the input file(s) resides in the same folder as the program. 
This program executes Strassen’s method of matrix multiplication as well as the naïve method of matrix multiplication only on square matrices that are a power of two. The user will be asked to provide file input in .txt form and provide the number of matrices in the file. The input text file contents must be formatted in row major order, with the order of the matrices at the top, followed directly by a newline and the first row of the first matrix with a single space between values. The two matrices to be multiplied should not have a blank line between them, but matrix couples should be separated by a new line. For example: 
2 
1 2 
3 4
5 6 
7 8

4
1 2 3 4
5 6 7 8 
4 3 2 1
8 7 6 5

…

This program has three functions total: 
divide_matrix
Strassen_method
matrix_multiplication
The “divide_matrix” function is responsible for determining the shape (i.e. the order) of the input matrices and dividing them by two. This function is called in the “Strassen_method” function and returns a submatrix of size order/2. 
The “Strassen_method” function takes two square matrices of the same size whose order is a power of 2 as arguments and implements Strassen’s method for matrix multiplication. This function is called recursively, whose number of calls depends on the original size of the input matrices and returns the product once the matrix size equal one. There are a total of seven calls to the “Strassen_method” function (values p1-p7) for each division of the matrix, where each must run recursively until the base case is reached, in which multiplication is then done. Once values p1-p7 are obtained, they are arithmetically manipulated and combined to generate the final product matrix, “C”, which gets returned. 
The “matrix_multiplication” method takes two square matrices of the same size and whose order is a power of 2 as arguments and implements naïve matrix multiplication. An empty matrix of dynamic size is first initialized to hold the product. The function then traverses through the rows of the first matrix and the columns and rows of the second matrix, summing up the products with each iteration. The final product, “product” is returned.
This program does not print to the terminal but writes the output of both multiplication methods as well as execution times and number of multiplications per method to a text filed named “products” for visualization. 
