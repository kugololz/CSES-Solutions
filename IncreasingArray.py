import sys

n = int(input())
numbers= [int(x) for x in sys.stdin.readline().split()]
contador = 0


for x in range(1, n):
    while(numbers[x] < numbers[x-1]):
        diferencia = (numbers[x-1] - numbers[x])
        numbers[x] += diferencia
        contador += diferencia

print(contador)