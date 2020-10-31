for sayı1 in range(10,100):
	s1 = str(sayı1)
	for sayı2 in range(10,100):
		s2 = str(sayı2)
		if int( s1+s2 ) == ( int(sayı1) + int(sayı2) ) * 11:
			print("sayı1=",sayı1,"\nsayı2=",sayı2)
