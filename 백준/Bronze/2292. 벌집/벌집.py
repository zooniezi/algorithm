a = int(input())
layer = 0
index = 1
while True:
    if a == 1:
        print(1)
        break
    if index >= a:
        print(layer)
        break
    index += 6*layer
    layer+=1

