# Palindrome
# it simply means when the number is reversed it is SAME.
# 12321 == 12321, 333 == 333, 787 = 787

num = int(input('Enter a number : '))
temp = num
rev = 0

# ex: num = 123
while num > 0:
    dig = num % 10              # qill give the last digit, deg = 3
    rev = rev*10 + dig          # will write the last number at first, rev = 3
    num = num//10               # will remove the last digit, num = 12

if num == temp :
    print('Number is Palindrome...!')
else :
    print('Number is not palindrome...!')
