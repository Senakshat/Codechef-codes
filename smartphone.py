n=int(input())
a=[]
for i in range(n):
    t=int(input())
    a.append(t)
l=len(a)
m=0
t1=0
t2=0
a.sort()
if(l%2==0):
    m=int(l/2)
    m1=int(l/2+1)
    t1=a[m-1]*(l-m+1)
    t2=a[m1-1]*(l-m1+1)
    if(t1>=t2):
        print(t1)
    else:
        print(t2)
else:
    m=int(l/2+1)
    t1=a[m-1]*(l-m+1)
    print(t1)
        
        
    
    
    
