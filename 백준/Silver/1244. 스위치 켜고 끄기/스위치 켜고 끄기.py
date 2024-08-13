num_of_switch = int(input())
switch = list(map(int,input().split()))
num_of_students = int(input())
for _ in range(num_of_students):
    gender, number = map(int, input().split())
    if gender == 1:
        check = number
        while check-1 < num_of_switch:
            switch[check-1] = -switch[check-1]+1
            check += number
    else: #gender = 2
        temp = 1
        switch[number-1] = -switch[number-1]+1
        while True:
            if 0<= number-temp-1<num_of_switch and 0<=number+temp-1<num_of_switch:
                if switch[number-temp-1] == switch[number+temp-1]:
                    switch[number-temp-1] = -switch[number-temp-1]+1
                    switch[number+temp-1] = -switch[number+temp-1]+1
                    temp+=1
                else:
                    break
                
            else:
                break

if num_of_switch <= 20:
    print(*switch)
else:
    for i in range(num_of_switch):
        if i != 0 and i%20==0:
            print()
        print(switch[i], end=" ")