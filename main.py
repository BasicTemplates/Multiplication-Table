n = int(input("Введите число: "))

for i in range(1, n+1):
     print(*range(i, i*n+1, i), sep='\t')