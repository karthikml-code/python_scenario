def duplicate(sample):
    org_set = set()
    for i in sample:
        #print(i)
        if i in org_set:
            return i
        else:
            org_set.add(i)
            #print(org_set)
    return None
