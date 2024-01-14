count = 0

largest1 = 0

largest2 = 0

while count <= 10:

	number = int(input("Enter number: "))
		
	if number > largest1:
		largest2 = largest1
		largest1 = number
	
	elif number > largest2: 
		largest2 = number

	

	count += 1

print(f'the first largest is{largest1}')
print(f'the second largest is{largest2}')