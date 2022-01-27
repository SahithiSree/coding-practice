a,b=0,1

n=int(input())
print(a)
print(b)
for i in range(2,n):
    c=a+b
    print(c)
    a,b=b,c
