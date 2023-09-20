def main():

    ##############################
    # make your code below
    # print('Hello World')
    ##############################
    print ('Hello World')

    # num1 = int(input('Enter the number 1 :'))
    # num2 = int(input('Enter the number 2: '))
    # num2 = int(input('Enter the number 3: '))
    num1 = 5
    num2 = 9
    num3 = 1

    if num1 < num2:
        if num1 < num3:
            minval = num1
        else:
            minval = num3
    else:
        if num2 < num3:
            minval = num2
        else:
            minval = num3
    print (minval)                        

if __name__ == '__main__':
    main()
