def print_secDiag(mat):
    n = len(mat)
    n = n -1
    count = 0

    while(count<=3):

        print(mat[count][n])
        count += 1
        n -= 1



mat1 = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
print_secDiag(mat1)