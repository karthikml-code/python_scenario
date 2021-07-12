def digits_sum(string):
    summ = 0
    digits = [int(i) for i in string.split() if i.isdigit()]
    for i in digits:
        summ +=i
    return summ
