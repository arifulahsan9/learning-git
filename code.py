# find duplicates from a list in Python

l=[1,2,3,4,5,2,3,2,4,7,9,5]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
    else:
        print(i,end=' ')

print('\n')

# Using set()
l=[1, 3, 2, 6, 2, 3, 5, 6, 4, 5]
print(set([x for x  in l if l.count(x)>1]))

# use the Counter() function
from collections import Counter

li=[1, 3, 2, 6, 2, 3, 5, 6, 4, 5]
d = Counter(li)

repeated_list = list([num for num in d if d[num]>1])
print("Duplicate integers: ",repeated_list)
