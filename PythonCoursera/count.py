import math
n = int(input("Enter n: "))
sum = 0.0
for i in range(1, n+1):
    sum += math.log10(i)
print(int(sum)+1)
