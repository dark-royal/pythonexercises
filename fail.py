number = int(input("Enter scores: enter 0 to end program"))

studentPass = 0

fail = 0




while number != 0:
	if number < 0:
		print("invalid input")
	elif number > 100:
		print("invalid input")
	elif number >= 45:
		studentPass += 1
	elif number < 45:
		fail += 1
	number = int(input("Enter scores"))
	

	
	


print("the number of student that pass is", studentPass)
print("the number of student that failed is", fail)