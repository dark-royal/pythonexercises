import random
frequency1 = 0
frequency2 = 0
frequency3 = 0
frequency4 = 0
frequency5 = 0
frequency6 = 0

for roll in range(6_000_000):
	face = random.randrange(1, 7)

	if face == 1:
		frequency1 += 1
	elif face == 2:
		frequency2 += 1

	elif face == 3:
		frequency3 += 1

	elif face == 4:
		frequency4 += 1

	elif face == 5:
		frequency5 += 1

	elif face == 6:
		frequency6 += 1

print(f' face{"frequency":>13}')
print(f'{1 :>13}{frequency1 :>13}')