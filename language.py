language = input("Enter your preferred language")

match language:
	case 'java':
		print("A java pro",end=',')

	case 'python':
		print("phytonista")
	case _:
		print("this is default")