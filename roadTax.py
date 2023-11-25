price = int(input("Enter the price of the car"))

if(price < 1000000):
	number1 = price * 10/100
	print(number1)

elif(price >= 1000000 and price <= 3000000):
	number2 = price * 15/100
	print(number2)

elif(price >= 3000000 and price <= 5000000):
	number3 = price * 20/100
	print(number3)

elif(price >= 5000000):
	number4 = price * 25/100
	print(number4)

