#Hazelyn Cates
#EN.605.620.81.FA22
#Started 9/11/22
#This program implements Strassen's method of matrix multiplication and naive matrix multiplication

import numpy as np
import math as m
import re
import time

#record execution time of entire program
start_time = time.perf_counter()

#This function splits the matrices down by 1/2 every call
def divide_matrix(matrix):
    row, col = matrix.shape #gives order of matrix
    #print(row, col)

    row, col = row//2, col//2 #floor division of row and col to divide the matrix by 2

    #print(matrix[:row, :col], matrix[row:, :col], matrix[:row:, col:], matrix[row:, col:])
    return(matrix[:row, :col], matrix[:row, col:], matrix[row:, :col], matrix[row:, col:])
        #use array splitting to return submatrices


#This function implements Strassen's method using recursion
def Strassen_method(matrixA, matrixB):
    if matrixA.size == 1: #only have to check one matrix since matrix 1 and 2 are square matrices of the same size
        return(matrixA * matrixB) #once size = 1, that means the matrix has been broken down to its base case
                                  #so they get mulitplied together

    a, b, c, d = divide_matrix(matrixA) #call the "divide_matrix" function once per matrix to get submatrices
    e, f, g, h = divide_matrix(matrixB)
    #print(a, b, c, d)
    #print(e, f, g, h)

    #Call the Strassen_method function recursively until the arguments are 1x1 and can then be multiplied
    p1 = Strassen_method(a, f - h)
    p2 = Strassen_method(a + b, h)
    p3 = Strassen_method(c + d, e)
    p4 = Strassen_method(d, g - e)
    p5 = Strassen_method(a + d, e + h)
    p6 = Strassen_method(b - d, g + h)
    p7 = Strassen_method(a - c, e + f)

    C11 = p5 + p4 - p2 + p6
    C12 = p1 + p2
    C21 = p3 + p4
    C22 = p5 + p1 - p3 - p7

    #generate final product matrix
    C_final = np.hstack((np.vstack((C11, C21)), np.vstack((C12, C22))))

    return(C_final)


#This function implements naive matrix multiplication
def matrix_multiplication(matrix1, matrix2):
    r, c = matrix1.shape[0], matrix2.shape[1] #this establishes the rows of matrix 1 and the columns of matrix 2
                                              #in order to determine the size of the product matrix
    product = np.zeros((r, c))
    #this is the matrix that will hold the results of the multiplication
    #whose size varies depending on the matrices being multiplied and is initialized to contain all zeros

    #iterate through the rows of matrix1
    for i in range(len(matrix1)):
        #iterate through the columns of matrix2
        for j in range(len(matrix2[0])): #this starts at the first column of matrix2
            #iterate through the rows of matrix2
            for k in range(len(matrix2)):
                product[i][j] += matrix1[i][k] * matrix2[k][j] #sum products together

    return(product)


print("Enter full name of text file:")
file_name = input()
open_file = open(file_name, "r")

print("how many matrix couples in the file?")
answer = int(input())
#print(answer)

results_file = open("products.txt", "w") #this file holds the results of the Strassen method and naive multiplication

lineNum = 0 #this variable keeps track of which line of the file the inner for loop (on line 89) is on

for i in range(0, answer): #loops through all the matrix couples in the input file
    for line in open_file:
        lineNum += 1 #keeps track of line position in input file
                     #increment the line of the file by one for each pass through the inner for loop

        if (len(line) > 1 and (re.search(r' ', line) == None)): #Ensures that matrices with order above 9 are recognized
            order = int(line.strip('\n'))                       #without reading numbers from the matrices themselves
            #print ("\nMatrix order:  %d" % order)
            break

    if m.log2(order) != m.floor(m.log2(order)): #checks if matrix order is a power of 2
        #print("Matrix is not a power of 2")
        continue #if not, goes back to beginning of outer loop, skips the multiplication for those that aren't

    matrixA = np.loadtxt(file_name, skiprows=lineNum, max_rows=order, usecols=None) #reads in first matrix of the couple
    matrixB = np.loadtxt(file_name, skiprows=order + lineNum, max_rows=order, usecols=None) #reads in second matrix of couple

    naive_count = order**3 #this counts the number of multiplications for the naive method
    Strassen_count = order**(m.log2(7)) #this counts the number of multiplications for Strassen's method

    #call both functions and record execution time of each
    start_Strassen = time.perf_counter()
    Strassen_result = Strassen_method(matrixA, matrixB) #call Strassen_method function
    end_Strassen = time.perf_counter()
    total_Strassen = end_Strassen - start_Strassen #records total execution time for Strassen_method function

    start_naive = time.perf_counter()
    naive_result = matrix_multiplication(matrixA, matrixB) #call matrix_multiplication function
    end_naive = time.perf_counter()
    total_naive = end_naive - start_naive #records total execution time for matrix_multiplication function

    #Save results to output text filed named "products"
    results_file.write("\nMatrix order: %d\n" % order)
    results_file.write("Matrix multiplication product via Strassen's method:\nC =\n")
    np.savetxt(results_file, Strassen_result, fmt='%d')
    results_file.write("Number of multiplications for Strassen's method: %d" % Strassen_count)
    results_file.write("\n...\nTime to execute Strassen's method: %.2e seconds\n" % total_Strassen)

    results_file.write("\nVia naive multiplication method: \nC =\n")
    np.savetxt(results_file, naive_result, fmt='%d')
    results_file.write("Number of multiplication for naive method: %d" % naive_count)
    results_file.write("\n...\nTime to execute naive matrix multiplication: %.2e seconds\n" % total_naive)
    results_file.write("...........................................................................\n")


end_time = time.perf_counter() #record execution time of entire program
results_file.write("\nExecution time of entire program: %.2e seconds" % (end_time - start_time))

open_file.close()
results_file.close()