num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
num3 = int(input("Enter the third number"))

addition= num1 + num2 + num3

multiplication = num1 * num2 * num3

average = num1 + num2 + num3 / 3

if(num1 > num2 and num1 > num3):
	print("The largest number is",num1)

if(num2 > num1 and num2 > num3):
	print("The largest number is",num2)

if(num3 > num1 and num3 > num2):
	print("The largest number is",num3)

if(num1 < num2 and num1 < num3):
	print("The smallest number is",num1)

if(num2 < num1 and num1 < num3):
	print("The smallest number is",num2)

if(num3 < num1 and num3 < num2):
	print("The smallest number is",num3)





