for sayı1 in range(1,1000000):
	for sayı2 in range(1,1000000):
		if sayı1> sayı2 and sayı1 * sayı2 == 121212 and sayı1 - sayı2 < 50:
			print(sayı1,sayı2)
