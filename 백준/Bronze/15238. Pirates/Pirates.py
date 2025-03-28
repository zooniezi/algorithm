letter = [0 for i in range(26)]
n = int(input())
word = input()

for i in word:
    letter[ord(i)-97]+=1

maxnum = 0
maxidx = 0
for i in range(26):
    if letter[i]>maxnum:
        maxnum = letter[i]
        maxidx = i

print(chr(maxidx+97), maxnum)