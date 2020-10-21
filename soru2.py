Sum=0
for n in range(1,k):
	Sum+=(1/ n**2)

from math import sqrt
Pi=sqrt(Sum*6)
print("Pi sayısının yaklaşık değeri:",Pi)
