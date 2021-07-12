def palindrome_check(num):
    org = num
    rev = 0
    while(num>0):
        a = num%10
        rev = rev*10 + a
        num = num//10
    if rev == org:
        print('True')
    else:
        print('False')
