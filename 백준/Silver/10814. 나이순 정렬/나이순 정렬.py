n = int(input())

note = []
for i in range(n):
    age_name = list(map(str, input().split()))
    age_name[0] = int(age_name[0])
    note.append(age_name)
note.sort(key=lambda x:x[0])

for i in range(len(note)):
    print(note[i][0], note[i][1], sep=" ")
