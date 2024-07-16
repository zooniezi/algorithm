t = int(input())
words = []
sortedWords = []
for i in range(51):
    words.append([])

for i in range(t):
    nowWord = input()
    words[len(nowWord)].append(nowWord)

    
for i in range(51):
    if words[i] == []:
        continue
    else:
        temp = words[i]
        temp.sort()
        sortedWords += temp
        

for i in range(len(sortedWords)):
    if i == 0:
        print(sortedWords[i])
        continue
    elif sortedWords[i] == sortedWords[i-1]:
        continue
    else:
        print(sortedWords[i])

