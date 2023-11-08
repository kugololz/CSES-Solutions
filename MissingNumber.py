import sys

n = int(input())

numbers= [int(x) for x in sys.stdin.readline().split()]

total = sum(numbers)
suma = 0

for x in range(1, n+1):
    suma+=x

resultado = suma-total

print(resultado)