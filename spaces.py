number = int(input("Enter five digit number "))
89098

number1 = int(number / 10000)
remainder = int(number % 10000)

number2 = int(remainder / 1000)
remainder = int(remainder % 1000)

number3 = int(remainder / 100)
remainder = int(remainder % 100)

number4 = int(remainder / 10)
remainder = int(remainder % 10)

number5 = int(remainder / 1)
remainder = int(remainder % 1)

print( number1, number2, number3, number4, number5)
