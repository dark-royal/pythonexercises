count = 0
passes = 0
failures = 0
total = 0

number = int(input("enter number,1==passes and 2== failures"))

while count <= 10:
	

	if number !=1 and number != 2:

			number = int(input("enter number"))
	if passes == 1:
		passes += number

	else:
		total += failures
		print(passes)
		print(f'failures is {total}')

	count +=1