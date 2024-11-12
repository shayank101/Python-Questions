# list of prime numbers in range 1 to 100

def is_prime(n):
  '''
  This function will check the number is prime or not
  '''
    if n <= 1:
        return False

    for i in range(2,n):
        if n%i == 0:
            return False
    return True

lst1 = []

for i in range(100):
    if is_prime(i):
        lst1.append(i)

print(len(lst1))
print(lst1)
