passes = 0

failures = 0

for student in range(10):
	exam_result = int(input("Enter exam result(1==pass, 2 == fail): "))
	if exam_result == 1:
		passes += 1
	else: failures +=1

	print(f'number of passes is {passes}')
	print(f'number of failures is {failures}')

	if passes > 8:
		print("bonus to instructor")