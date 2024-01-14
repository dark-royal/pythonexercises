count = 0

amount = 0

rate = 7 / 100

years = 0


principal = int(input("Enter principal: "))

while principal != -1:
	years = int(input("Enter year: "))
	
	number = 1 * rate
	number_1 = principal * number
	
	amount = (principal * number_1) ** years


	print(f'the amount after {years}years is {amount}')
	
	principal = int(input("Enter principal: "))


	count += 1


