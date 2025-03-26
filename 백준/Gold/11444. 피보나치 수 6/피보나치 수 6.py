n = int(input())

def mat_mul(mat,mat2):
    return [
            [
            ((mat[0][0]*mat2[0][0])+(mat[0][1]*mat2[1][0]))%1000000007,
            ((mat[0][0]*mat2[0][1])+(mat[0][1]*mat2[1][1]))%1000000007
            ],
            [
            ((mat[1][0]*mat2[0][0])+(mat[1][1]*mat2[1][0]))%1000000007,
            ((mat[1][0]*mat2[0][1])+(mat[1][1]*mat2[1][1]))%1000000007
            ]
            ]

def fibo(n):
    if n == 1:
        return [[1,1], [1,0]]
    
    before_fibo = fibo(n//2)

    if n%2 == 1:
        return mat_mul(mat_mul(before_fibo,before_fibo),[[1,1],[1,0]])
    
    if n%2 == 0:
        return mat_mul(before_fibo,before_fibo)

print(fibo(n)[0][1])