n = int(input())
results = []
results.append(int(n))
 
while (n!=1):
    if(n%2 == 0):
        n = n/2
        results.append(int((n)))
    else:
        n = (n*3)+1
        results.append(int(n))

print(*results, sep=" ")