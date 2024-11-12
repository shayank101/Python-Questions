# Method 1
# using For
n = int(input('Enter a number : '))
factorial = 1

for i in range(1,n+1):
    factorial *= i

print(f'Factorial of {n} is {factorial}.')


# Method 2
# factorial using recursion

def fact(n):
    if n == 1:
        return 1
    else :
        return n * fact(n-1)

print(fact(5))
