#Return the element whose count is max in list

from collections import Counter
l1 = [3,3,3,2, 4, 4, 5]
d1 = Counter(l1)
print("dicer is ",d1)
max = 0
op = 0
for key,value in d1.items():
    if max < value:
        max = value
        op = key

print("key is ",op)
print("I am adding local changes")
print("Making changes in git ui 2nd time")




