sayı = input("Lütfen 3 veya 4 basamaklı bir sayı giriniz:")

if len(sayı) == 3:
    if int(str(sayı)[0]) == int(str(sayı)[-1]):
        print("Bu sayı palindromiktir!")
    else:
        print("Bu sayı palindromik değildir.")

elif len(sayı) == 4:
    if int(str(sayı)[0]) == int(str(sayı)[-2]) and int(str(sayı)[1]) == int(str(sayı)[-1]):
        print("Bu sayı palindromiktir!")
    else:
        print("Bu sayı palindromik değildir.")
              
