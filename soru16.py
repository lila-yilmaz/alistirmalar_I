counter = 0
sayı = int(input("Lütfen bir sayı giriniz: "))

for n in range(2,sayı):
           if (sayı%n)== 0:
               counter += 1
if counter == 0:
    print("Girdiğiniz sayı asaldır.")
else:
    print("Girdiğiniz sayı asal değildir!") 
               
