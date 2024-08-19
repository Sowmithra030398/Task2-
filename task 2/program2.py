#defining the prime number 
def is_prime(n):
    if n <= 1:
        return False  # 0 and 1 are not prime numbers
    for i in range(2,n-1):
        if n % i == 0:
            return False  # n is divisible by a number other than 1 and itself
    return True
# Input list
numbers = [10,501,22,37,100,999,87,351]
# Creating empty list for prime numbers
PrimeNumber = []
for number in numbers:
    if is_prime(number):
       PrimeNumber.append(number)

print("Prime Numbers are :",PrimeNumber) 



