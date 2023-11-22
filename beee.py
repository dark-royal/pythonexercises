number1 = int(input("Enter first number"))
number2 = int(input("Enter second number"))
number3 = int(input("Enter third number"))

max = number1
if(number2 > max):
max = number2

max = number2
if(number3 > max):
max = number3

max = number3
if(number1 > max):
max = number1