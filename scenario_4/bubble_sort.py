def bubblesort(x):
    n = len(x)
    for i in range(n-1):
        #print(f"i value {i}")
        for j in range(0,n-i-1):
        #print(f"j value {j}")
            if x[j] > x[j+1]:
                x[j+1],x[j] = x[j],x[j+1]
