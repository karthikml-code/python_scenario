import math
list1=[4,5,20,3,6,33,7]
even=0
odd=0
list2=[]
for i in list1:
    list2.append(i)
    if len(list2)>1 and len(list2)%2==0:
        even+=sum(list2)/len(list2)
    elif len(list2)>1 and len(list2)%2==1:
        odd += list2[math.ceil(len(list2)/2)-1]
    med= even+odd
