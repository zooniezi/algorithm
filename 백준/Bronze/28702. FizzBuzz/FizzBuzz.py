lines = []
for i in range(3):
    lines.append(input())

ans = 0

for i in range(3):
    if lines[i].isdigit():
        ans = int(lines[i])+3-i
        break

if ans%3 == 0 and ans%5 == 0:
    print("FizzBuzz")
elif ans%3 == 0:
    print("Fizz")
elif ans%5 == 0:
    print("Buzz")
else:
    print(ans)