def isCircular(path):
	x = 0
	y = 0
	for i in range(len(path)):
		move = path[i]

		if move == 'E':
			x += 1
		elif move == 'W':
			x -= 1
		elif move == 'N':
			y += 1
	print(x)
	print(y)
	return (x == 0 and y == 0)


path = input("ENTER A SEQ[N/E/W]:")
if isCircular(path):
	print("Given sequence of moves is circular")
else:
	print("Given sequence of moves is NOT circular")

