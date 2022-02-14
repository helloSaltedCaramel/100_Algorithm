a,m,d,n =map(int,input().split())
count = 1
while(count<n):
    a = (a*m)+d
    count +=1
print(a)
