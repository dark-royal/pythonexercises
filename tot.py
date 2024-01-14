total = 0

count = 0

array = {32, 45, 67, 21}

for item in array:
	total = total + item
	print(total)



while array[count] <= 4:
	total = total + array[count]
	print(total)

##do{
	##total = total + array[count]
	##print(total)
##} while array[count] != array.length -1