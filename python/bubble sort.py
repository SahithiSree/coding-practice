def bubblesort(li):
    for i in range(len(li)):
        for j in range(i,len(li)):
            if li[i]>li[j]:
                li[i],li[j]=li[j],li[i]
    return li
li=list(map(int,input().split()))
print(bubblesort(li))
