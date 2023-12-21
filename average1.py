count = 0
total = 0

product = 0

smallest = 0

largest = 0

while count <= 4:

	number = int(input("Enter number"))
	total += number
	
	print(f'the total is {total}')

	product *= number
	
	if number < smallest:
		number = smallest
		print( number)
	
	if number > largest:
		number = largest
		print(number)
	count += 1

	

print(f'the product is {product}')
	

	


average = total / count
print(average)