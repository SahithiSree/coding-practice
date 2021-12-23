#we check for an alternative postions characters or same starting from index 0

def mobilevirus(arr):
    for a in arr:
        good=1
        k=a[0]
        for i in range(0,len(a),+2):
            if k!=a[i]:
                good=0
                break
        print(good)
arr=list(map(str,input().split()))
mobilevirus(arr)

#input:['abadam',' madam','kljlil']
#output:
'''
1
0
0
'''

    
