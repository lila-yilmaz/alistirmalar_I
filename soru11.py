for X in range(2,125):
	kalan1=125%X
	kalan2=200%X
	kalan3=350%X
	if kalan1 == kalan2 == kalan3 and kalan1 != 0 and kalan1 > 10 and kalan1 < 125:
		print(X)
