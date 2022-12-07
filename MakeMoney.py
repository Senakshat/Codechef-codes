t=int(input())
for i in range(t):
    n=input().split()
    f=input().split()
    d=int(n[1])-int(n[2])
    a=[]
    c=0
    df=[]
    for h in f:
        df.append(h)
    for i in df:
        if(int(i)<d):
            a.append(n[1])
            c=c+1
            f.remove(i)
    f=f+a
    g=0
    for i in range(int(n[0])):
        g=g+int(f[i])
    tot=g-c*int(n[2])
    print(tot)
