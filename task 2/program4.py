userNumber = str(input("Enter the number ")) #defining the user input in the form of sting
print (userNumber)
first_digit=int(userNumber[0])#getting the first digit
# print(first_digit)
last_digit=int(userNumber[-1])#getting the last digit
Total_value=first_digit+last_digit#Adding the digits
print("The total of first and last digit",Total_value)