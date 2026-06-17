 # Question 1: Handle Division by Zero

# try:
#     num1= int(input("Enter number"))
#     num2= int(input("Enter number"))

#     result= num1/num2
#     print("Result=",result)

# except ZeroDivisionError as e:
#     print("Error")

# except ValueError as ab:
#     print("Invalid number")


# Question 2: Handle Invalid Number Input

# try:
#     num1=int(input("enter a number"))
#     print("nummber is=",num1)

# except ValueError as e:
#     print("invalid value")

# Question 3: Using try and except

# l1=[1,2,3,4,5]

# try:
   
#     num1=int(input("enter a index"))
#     print(l1[num1])

# except IndexError :
#     print("Index out of range")

# Question 4: Using else Block

# try:
#     num1 = int(input("Enter a Number"))
#     num2 = int(input("Enter 1st number: "))
#     result = num1 / num2
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except ValueError:
#     print("Invalid Input")
# else:
#     print("Result = ", result)


# Q6 Multiple Exceptions

# l1 = [1, 2, 3]
# ind1 = int(input("Enter index: "))
# try:
#     num1 = int(input("Enter a Number: "))
#     l1.insert(num1, ind1)
# except ValueError or IndexError:    
#     if ValueError:
#         print("Invalid input")
#     else:
#         print("Index out of range")

# Question 7: Custom Exception

# class InvalidAgeError(Exception):
#  pass

# age = 15
# if age<18:
#   raise InvalidAgeError("Age must be greater than 18")
