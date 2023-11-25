number = int(input("Enter the integer numbers"))

total = 0
count = 0

while number != 0:
	total += number
	count += 1
	number = int(input("Enter the integer numbers"))

sum = total
average = total/ count

print("the sum is", sum)
print("the average is", average)
