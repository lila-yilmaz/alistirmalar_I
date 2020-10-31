for n in range(1,1000):
	if n in range(1,10) and int(str(n)[0]) < 9 :
		print(n)
	elif n in range(10,100) and int(str(n)[0]) + int(str(n)[1]) < 9 :
		print(n)
	elif n in range(100,1000) and int(str(n)[0]) + int(str(n)[1]) + int(str(n)[-1]) < 9 :
		print(n)
