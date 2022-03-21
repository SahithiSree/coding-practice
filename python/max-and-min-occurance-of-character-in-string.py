s='wileymthree'
freq=[]
min_str=""
max_str=""
for i in s:
    a=s.count(i)
    freq.append(a)
mi=min(freq)
ma=max(freq)
print(mi,ma)


#single element occurance
a=freq.index(mi)
b=freq.index(ma)
print(s[a],s[b])


#multiple element min and max occurence

for j in range(len(freq)):
    if freq[j] == mi:
        min_str=min_str+s[j]
    elif freq[j]==ma:
        max_str=max_str+s[j]
      
print(set(min_str),set(max_str))
