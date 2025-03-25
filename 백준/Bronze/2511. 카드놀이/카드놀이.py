a = list(map(int,input().split()))
b = list(map(int,input().split()))

score_a, score_b = 0,0
winner = 0
for i in range(10):
    if a[i]>b[i]:
        score_a+=3
        winner=1
    elif a[i]<b[i]:
        score_b+=3
        winner=2
    else:
        score_a+=1
        score_b+=1

print(score_a,score_b)
if score_a>score_b:
    print('A')
if score_a<score_b:
    print('B')
if score_a==score_b:
    if winner==1:
        print('A')
    elif winner == 2:
        print('B')
    else:
        print('D')