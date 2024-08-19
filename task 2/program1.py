# Input list
numbers = [10,501,22,37,100,999,87,351]

# Creating two empty sets
evenNumbers = []
oddNumbers = []

# Programme using %
for number in numbers:
    if number % 2 == 0:
        # If the number is even append to below list
        evenNumbers.append(number)
    else:
        # If the number is odd append to below list
        oddNumbers.append(number)

# Results
print("Even numbers:", evenNumbers)
print("Odd numbers:", oddNumbers)
