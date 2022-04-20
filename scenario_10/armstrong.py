def armstrong_check(arr):
    try:
        if type(arr) == list:
            for item in range(len(arr)):
                temp=0
                for i in str(arr[item]):
                    temp +=int(i)**3
                if temp == arr[item]:
                    print(f'{arr[item]} is an armstrong number')
                else:
                    print(f'{arr[item]} is not an armstrong number')
        else:
            print("Please enter in list format")
    except:
        print("Please enter in list format")
