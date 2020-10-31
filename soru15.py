for sayı in range(10000,100000):
        asal=True
        for i in range(2,sayı):
            if sayı % i == 0:
                    asal=False
        if asal == True:
                print(sayı)
                
                        
