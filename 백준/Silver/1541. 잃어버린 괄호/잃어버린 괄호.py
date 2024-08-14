expression = input()

arr = list(expression.split("-"))
translate_arr = []
for each in arr:
    l = len(each)
    nownum = []
    result = 0
    for i in range(l):
        if each[i]!='+':
            nownum.append(each[i])
        else:
            result += int("".join(nownum))
            nownum = []
    if nownum:
        result += int("".join(nownum))
        nownum = []
    translate_arr.append(result)

ans = translate_arr[0]
for i in range(1,len(translate_arr)):
    ans-=translate_arr[i]
print(ans)
