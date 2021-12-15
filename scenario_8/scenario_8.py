a = [1,2,3,4,5,6,7,8,9]
#taking the length of the list
n = len(a)
#splitting the list in half for reversing
for i in range(int(n/2)):
    #switching the positions of the items in the list
    a[i],a[n-i-1] = a[n-i-1], a[i]
print(a)
