unit = int(input("Enter a unit"))

if( unit < 100):
	print("no charges")

if(unit > 100 and unit < 200):
	amount = (unit - 100) * 10

if(unit > 200):
	unit = unit - 100

	amount = (100 * 10) + (unit - 100) * 20

	print(amount)