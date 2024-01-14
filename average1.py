count = 0
total = 0

product = 1

smallest = 0

largest = 0

while count <= 4:

	number = int(input("Enter number"))
	smallest = number
	total += number
	
	

	product *= number
	
	
	count += 1
	
if number > largest:
	largest = number
	
	
	
if number > smallest:
	smallest = number
	
	

	

	

	
average = total / count

print(f'the average is{average}')

print(f'the product is {product}')

print(f'the total is {total}')
print(f'the smallest is{smallest}')
print(f'the largest is{largest}')
