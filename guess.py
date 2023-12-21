from random import randint

counter = 0

guessNumber = randint(1,4)

while counter <= 3:
	number = int(input("Enter guess: "))


	if number == guessNumber:
		print("you won!")
	
	if number > guessNumber:
		print("incorrect,try again")

	if number < guessNumber:
		print("incorrect,try again")

	counter = counter + 1
	 
