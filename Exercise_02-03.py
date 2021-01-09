import numpy as np
import sys

row_counter = 0
col_counter = 0

level = 1
while level<3 :
    
    if   level == 1 : text = "Please enter a Matrix:"
    
    elif level == 2 :
        text  = "Please Enter Another Matrix With Dimensions "
        text += "{0}x{1}:".format(col_counter, row_counter)
        
    text += "\n* Example For Input Format Of a 2x3 Matrix:\n"
    text += "[[0 0 1],[1 0 0]]\n\n"
    
    inpt = input(text)
    
    lst = []
    row = []

    row_counter = 0
    col_counter = 0
    for i in range(len(inpt)):
         
        if (inpt[i] == ']') & (inpt[i-1] != ']') :
            lst.append(row)    
            row = []
            row_counter += 1
            if inpt[i+1] != ']' : col_counter = 0
            
        elif (inpt[i] != ' ') & (inpt[i] != ',') & (inpt[i] != '[') & (inpt[i] != ']') :
            row.append(int(inpt[i]))
            col_counter += 1
    
    matrix = np.array(lst) #Convert list to matrix
    
    if   level == 1 :
        matrix_A = matrix
        row_A = row_counter
        col_A = col_counter
        
    elif level == 2 :
        matrix_B = matrix
        row_B = row_counter
        col_B = col_counter
        
        if (col_B != row_A) | (row_B != col_A):
            print("\n*********************************")
            print(">>> ERROR!")
            print("The Dimensions Of The First Matrix And The Second Matrix Do Not Fit Together!")
            print("Dimensions Of The First  Matrix: {0}x{1}".format(row_A,col_A))
            print("Dimensions Of The Second Matrix: {0}x{1}".format(row_counter,col_counter))
            print("\n>>> Run The Program Again...")
            print("*********************************")
            sys.exit(0)
    
#Save the given matrix in sparse form:

    nnz = 0
    lst = [[row_counter, col_counter, nnz]]
    
    for row in range(len(matrix)):
        
        for colomn in range(len(matrix[row])):
            
            if matrix[row][colomn] != 0 :
                lst.append([row, colomn, matrix[row][colomn]])
                nnz += 1
                
    lst[0][2] = nnz
            
    sparse = np.array(lst) #Convert list to matrix
    
    if   level == 1 : sparse_A = sparse
    elif level == 2 : sparse_B = sparse
    
    level += 1 # Get the second matrix (with While loop)    

# 5.Multiply sparse matrix A and sparse matrix B: ---------------------------------

nnz = 0
lst = [[row_A, col_B, nnz]]
        
for row_SA in range(len(sparse_A)):
    
    if 0 < row_SA:
        
        row_A = sparse_A[row_SA][0] 
        col_A = sparse_A[row_SA][1]
        val_A = sparse_A[row_SA][2]
        
        for row_SB in range(len(sparse_B)):
            
            if 0 < row_SB:

                row_B = sparse_B[row_SB][0] 
                col_B = sparse_B[row_SB][1]
                val_B = sparse_B[row_SB][2]
    
                if col_A == row_B :
                    
                    MUL = val_A * val_B
                    lst.append([row_A, col_B, MUL])
                    nnz += 1
                    
i = 0
for value_1 in lst:

    if 0 < i:

        row_1 = value_1[0] 
        col_1 = value_1[1]
        val_1 = value_1[2]

        SUM = 0
        j = 0
        for value_2 in lst:
            
            if 0 < j:
                
                row_2 = value_2[0] 
                col_2 = value_2[1]
                val_2 = value_2[2]
                
                if (row_1 == row_2) & (col_1 == col_2) & (i < j) :
                    
                    SUM = val_1 + val_2 + SUM
                    lst[i][2] = SUM
                    del lst[j]
                    nnz -= 1
            j += 1
        
    i += 1

lst[0][2] = nnz                
mul_sparse = np.array(lst) #Convert list to matrix
                
print("\nYour First  Matrix (A):")
print(matrix_A)
print("\nYour Second Matrix (B):")
print(matrix_B)
print("\nMultiply Sparse Matrix A And Sparse Matrix B:")
print(mul_sparse)      
        


