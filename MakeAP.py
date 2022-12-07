t=int(input())
for i in range(t):
    n=input().split()
    ap=(int(n[1])-int(n[0]))/2
    b=int(ap)
    if(float(b)<ap):
        print(-1)
    else:

        print(int(n[0])+b)
