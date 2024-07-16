test = input()
num = []
word = test.upper()
ideaWord = list(set(word))
for i in ideaWord:
    amount = word.count(i)
    num.append(amount)
if num.count(max(num)) > 1:
    print("?")
else:
    maxi = num.index(max(num))
    print(ideaWord[maxi])
