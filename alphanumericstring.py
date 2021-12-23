#seperating alphanumeric string & printing the string & some of the digits

a=input().split()
num=[]
str=[]
sum=0
for i in a:
    if i.isdigit()==True:
        sum+=int(i)
    else:
        str.append(i)
op=''.join(str)
print(op)
print(sum)


#input:2018 India 18 is my country
#output:
#indiaismycountry
#2036
