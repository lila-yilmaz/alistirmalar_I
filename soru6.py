counter=0

for n in range(1000,10000):
	if int(str(n)[0]) > int(str(n)[-1]):
		counter+=1

print(counter)
