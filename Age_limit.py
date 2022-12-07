n=int(input())
for i in range(n):
    j=input().split()
    if int(j[2])>=int(j[0])and int(j[2])<int(j[1]):
        print("YES")
    else:
        print("NO")
