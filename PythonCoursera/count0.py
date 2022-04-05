def zero(n):
    count = 0
    if n < 5:
        return 0
    for i in range(5, n+1, 5):
        while i % 5 == 0:
            count = count+1
            i /= 5
    return count
n = int(input("Enter n: "))
print(zero(n))
