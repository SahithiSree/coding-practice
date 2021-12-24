#take an alphanumeric string and print the index of an integers in an string


a=input()
res=""
for i in range (len(a)):
    if a[i]>='0'and a[i]<='9':
        res=res+str(i)
print(res)

#input:abc45t6y7hy09
#ouput:34681112
