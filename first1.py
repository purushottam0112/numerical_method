# def addition_of_matrics():
#     m1, n1 = input("Enter size of first matrix: ").split()
#     print("Enter first matrix: ")
#     matrix_A = [input().split() for i in range(int(m1))] 
#     m2, n2 = input("Enter size of second matrix: ").split()   
#     print("Enter second matrix: ") 
#     matrix_B = [input().split() for i in range(int(m2))] 
#     if m1 == m2 and n1 == n2:
#         print("The result is: ")
#         sum = [[0 for j in range(int(n1))] for i in range(int(m1))]
#         for i in range(int(m1)):
#             for j in range(int(n1)):
#                 sum[i][j] = str(float(matrix_A[i][j]) + float(matrix_B[i][j]))
#             print(" ".join(sum[i]))
#     else:
#         print('The operation cannot be performed.')      
#     return main()

# def Multiply_matrix_by_constant():
#     m1, n1 = input("Enter size of first matrix: ").split()
#     print("Enter first matrix: ")
#     matrix_A = [input().split() for i in range(int(m1))]
#     c = int(input())
#     print("The result is: ")
#     scalar_product = [[0 for j in range(int(n1))] for i in range(int(m1))]
#     for i in range(int(m1)):
#         for j in range(int(n1)):
#             scalar_product[i][j] = c * float(matrix_A[i][j])
#         print(*scalar_product[i])    
#     return main()



def Multiplication_of_two_matrix(matrix_A, matrix_B):
    import numpy as np
    m1 = len(matrix_A)
    n1 = len(matrix_A[0])

    m2 = len(matrix_B)
    n2 = len(matrix_B[0])
    if n1 == m2:
        product = [[0 for j in range(int(n2))] for i in range(int(m1))]
        for i in range(int(m1)):
            for k in range(int(n2)):
                sum = 0
                for j in range(int(n1)):
                    sum += float(matrix_A[i][j]) * float(matrix_B[j][k])
                product[i][k] = sum
        return np.array(product)
    else:
        print("The operation cannot be performed.")        

  

    
# def Transpose_of_matrix():
#     print('''1. Main diagonal
# 2. Side diagonal
# 3. Vertical line
# 4. Horizontal line''')
#     action = input("Your choice: ")
#     m1, n1 = input("Enter matrix size: ").split()
#     print("Enter matrix: ")
#     matrix_A = [input().split() for i in range(int(m1))]

#     if action == "1":
#         transpose_matrix = [[matrix_A[j][i] for j in range(int(n1))] for i in range(int(m1))] 
#         for i in range(int(n1)):
#             print(*transpose_matrix[i])
#         return main()
         
#     elif action == "2":
#         matrix = [[matrix_A[j][i] for j in range((int(n1)-1), -1, -1)] for i in range((int(m1)-1), -1, -1)]  
#         for i in range(int(n1)):
#             print(*matrix[i])
#         return main()

#     elif action == "3":
#         matrix = [[matrix_A[i][j] for j in range((int(n1))-1, -1, -1)] for i in range(int(m1))]  
#         for i in range(int(m1)):
#             print(*matrix[i])  
#         return main()

#     elif action == "4":
#         matrix = [[matrix_A[i][j] for j in range(int(n1))] for i in range((int(m1)-1), -1, -1)]    
#         for i in range(int(m1)):
#             print(*matrix[i])         
#         return main()  

# def determinant():
#     def det(A):
#         n = len(A)
#         if n == 1:                                       
#             res = A[0][0]         
#             return res                                   
#         res = 0 
#         row = []
#         delete_row = A.pop(0)
#         row.append(delete_row)  # row = [[a0, a1, a2, a3, ..... ]]
        
#         for j in range(n):
#             col = []
#             for k in range(n-1):
#                 delete_columb = A[k].pop(j) # delete columb
#                 col.append(delete_columb)   
#             res += (-1)**(0+j) * row[0][j] * det(A)
#             for m in range(n-1):
#                 (A[m]).insert(j, col[m])
#         A.insert(0, row[0])        
#         return res

#     print("Enter the size of determinat")
#     m1, n1 = input().split()
#     if m1 == n1:
#         print("Enter matrix: ")
#         A = [[float(x) for x in input().split()] for y in range(int(m1))]
#         print("The result is:")
#         print(det(A))
#     else:
#         print("The operation cannot be performed.") 
#     return main()

# def main():
#     print('''1. Add matrices
# 2. Multiply matrix by a constant
# 3. Multiply matrices
# 4. Transpose matrix 
# 5. Calculate a determinant
# 0. Exit''')
#     action = input("Your choice: ")
#     if action == "1":
#         addition_of_matrics()
#     elif action == "2":
#         Multiply_matrix_by_constant()
#     elif action == "3":
#         Multiplication_of_two_matrix()
#     elif action == "4":
#         Transpose_of_matrix()  
#     elif action == "5":
#         determinant()      
#     else:
#         return  
        
# main()