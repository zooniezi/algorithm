import sys

sticks = sys.stdin.readline()[:-1]
check_stick = 0
num_of_sticks = 0

def laser():
    global num_of_sticks
    global check_stick
    num_of_sticks += check_stick


for i in range(len(sticks)):
    if i < len(sticks)-1:
        if sticks[i] == '(' and sticks[i+1] == ')':
            laser()
            continue
    if i > 0:
        if sticks[i] == ')' and sticks[i-1] == '(':
            continue
    if sticks[i] == '(':
        check_stick += 1
    if sticks[i] == ')':
        check_stick -= 1
        num_of_sticks += 1
    
print(num_of_sticks)

