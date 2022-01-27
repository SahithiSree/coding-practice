def str(s,l):
    for i in range(0,l):
       if s[i] != s[l-i-1]:
        return False
    return True
    
s=input()
l=len(s)
res=str(s,l)
print(res)
