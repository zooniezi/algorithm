line = input()
arr = []
for i in range(len(line)):
    arr.append(line[i:])

arr.sort()
for each in arr:
    print(each)