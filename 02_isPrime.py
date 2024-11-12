# Check whether the number given by user is Prime or not 

num = int(input('Enter a number you want to check prime : '))

if num < 0:
    print('Not prime')
elif num == 1:
    print('Is prime')
else : 
    for i in range(2,num//2):
        if num%i==0:
            print("Not prime...")
            break
    else :
        print("Is prime")
