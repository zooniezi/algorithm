import sys
input = sys.stdin.readline

n,b = map(int,input().split())
mat = [list(map(int,input().split())) for i in range(n)]
def matrix_product(matrix1, matrix2):
    ans = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                ans[i][j] += (matrix1[i][k]*matrix2[k][j])%1000
            ans[i][j]%=1000
    return ans

def get_ans(matrix,power):
    if power == 1:
        return matrix
    if power == 2:
        return matrix_product(matrix,matrix)
    a = get_ans(matrix,power//2)
    if power % 2 == 0:
        return matrix_product(a,a)
    else:
        return matrix_product(matrix_product(a,a),mat)

ans = get_ans(mat,b)
for i in range(n):
    for j in range(n):
        print(ans[i][j]%1000, end=" ")
    print()