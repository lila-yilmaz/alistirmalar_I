counter = 0

for n in range(10000,100000):
	if int(str(n)[0]) == int(str(n)[-2]) and int(str(n)[1]) == int(str(n)[-2]):
		counter += 1


print(counter)
