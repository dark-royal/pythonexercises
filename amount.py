principal = 1000
rate = 5 /100

for year in range(1, 11):
	amount = principal * (1 + rate) ** year
	print(f'{year:>2}{amount :> 10.2f}')
