import random
if __name__ == '__main__':
    l = []
    for _ in range(4):
        tmp = []
        for _ in range(random.randint(2,3)):
            tmp.append(random.randint(1,9))
        l.append(tmp)

print(l)
s = sorted(sorted(sorted(l,key = sum), key = min), key = max)

print(s)

l2 = []
l2.append(sorted(sorted(sorted(l,key=sum),key=min),key=max))
l2.append(sorted(sorted(sorted(l,key=sum),key=max),key=min))
l2.append(sorted(sorted(sorted(l,key=max),key=min),key=sum))
l2.append(sorted(sorted(sorted(l,key=max),key=sum),key=min))
l2.append(sorted(sorted(sorted(l,key=min),key=sum),key=max))
l2.append(sorted(sorted(sorted(l,key=min),key=max),key=sum))

print(len(set([str(x) for x in l2])))
print(l2)
print(sorted(l2))