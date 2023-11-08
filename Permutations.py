n = int(input())
pairs = []
no_pairs = []

if(n > 3 or n==1):
    for x in range(1, n+1):
        if (x%2 == 0):
            pairs.append(x)
        else:
            no_pairs.append(x)

    result = pairs + no_pairs
    print(*result, sep=" ")

else:
    print("NO SOLUTION")


