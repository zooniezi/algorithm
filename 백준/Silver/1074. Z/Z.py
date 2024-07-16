N, r, c = map(int, input().split())

order = 0

while True:
    if N == 0:
        break
    N = N-1

    if r<2**N and c<2**N:
        continue
    elif r<2**N and c>=2**N:
        order = order + 2**(2*N)
        c = c-2**N

    elif r>=2**N and c<2**N:
        order = order + 2**(2*N)*2
        r = r-2**N
    elif r>=2**N and c>=2**N:
        order = order + 2**(2*N)*3
        c = c - 2 ** N
        r = r - 2 ** N

print(order)