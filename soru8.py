counter = 0

for n in range(100,1000,2):
    if int(str(n)[0]) == int(str(n)[-1]):
        counter += 1
    elif int(str(n)[1]) == int(str(n)[-1]):
        counter += 1
    elif int(str(n)[1]) == int(str(n)[0]):
        counter += 1


print(counter)
