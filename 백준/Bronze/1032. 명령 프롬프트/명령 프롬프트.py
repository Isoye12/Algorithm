n = int(input())
result = list(input())

for i in range(n-1):
    a = list(input())
    for i in range(len(result)):
        if(i>=len(a)): result[i] = '?'
        if(result[i]!=a[i]):
            result[i] = '?'

for i in result:
    print(i, end="")