import collections
n,p,q = map(int,input().split())

dictionary = collections.defaultdict(int)
dictionary[0] = 1

def infSequence(n,p,q):
    if dictionary[n]!=0:
        return dictionary[n]
    dictionary[n] = infSequence(n//p,p,q) + infSequence(n//q,p,q)
    return dictionary[n]

print(infSequence(n,p,q))