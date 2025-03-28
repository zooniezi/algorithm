n,d = map(int,input().split())

for i in range(n):
    word = input()
    ans = ''
    for i in word:
        if d == 1:
            if i == 'd':
                ans+='q'
            if i == 'q':
                ans+='d'
            if i == 'b':
                ans+='p'
            if i == 'p':
                ans+='b'
        if d == 2:
            if i == 'd':
                ans+='b'
            if i == 'q':
                ans+='p'
            if i == 'b':
                ans+='d'
            if i == 'p':
                ans+='q'
    print(ans)

