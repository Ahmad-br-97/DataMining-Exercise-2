import numpy as np

text = "Please Enter a Matrix:"
text += "\n* Example For Input Format Of a 2x3 Matrix:\n"
text += "[[0 0 1],[1 0 0]]\n\n"

# 1.Get sparse matrix from user with input() function: ----------------------

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
  
print("\nYour Matrix:")
print(matrix)

# 2.Save the given matrix in sparse form: ------------------------------------

nnz = 0
lst = [[row_counter, col_counter, nnz]]

for row in range(len(matrix)):
    
    for colomn in range(len(matrix[row])):
        
        if matrix[row][colomn] != 0 :
            lst.append([row, colomn, matrix[row][colomn]])
            nnz += 1
            
lst[0][2] = nnz
        
sparse = np.array(lst) #Convert list to matrix
      
print("\nSparse:")
print(sparse)
            
# 3.Calculate matrix transpose: ----------------------------------------------

lst = []

for row in range(len(sparse)):
    
    lst.append([sparse[row][1], sparse[row][0], sparse[row][2]])

transpose_sparse = np.array(lst)
      
print("\nTransmission:")
print(transpose_sparse)    
                
            
            
        


