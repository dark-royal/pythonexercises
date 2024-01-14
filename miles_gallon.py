count = 0

total_miles = 0

total_gallon = 0

total_miles_per_gallon = 0

gallon = 0

miles_per_gallon = 0

miles = int(input("Enter miles(-1 to end): "))

while miles != -1:

	total_miles += miles

	gallon = int(input("Enter gallon: "))
	total_gallon += gallon

	miles_per_gallon = miles / gallon
	
	print(f'The miles/gallon is {miles_per_gallon}')

	total_miles_per_gallon += miles_per_gallon

	miles = int(input("Enter miles(-1 to end): "))


	count += 1

print(f'The overall average miles/gallon was {total_miles_per_gallon}')



	

	

