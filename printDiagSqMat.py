def print_diag(mat):
    n = len(mat)
    for i in range(n):
        for j in reversed(range(n)):
            if (i == j):
                print (mat[i][j])
    
    

mat1 = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
print_diag(mat1)