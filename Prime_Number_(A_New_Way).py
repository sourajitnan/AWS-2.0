n=int(input())
for i in range(2,n):
    if n%i==0:
        x=(' is not a prime number')
        break
    else:
        x=(' is a prime number')
print(x)