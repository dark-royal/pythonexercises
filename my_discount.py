def my_discount(price, discount):
	discount = price * discount
	return discount

	percentage_discount = price - discount
	return percentage_discount

price = 150
discount = 15/100
print(my_discount(price, discount))