a,b,c = map(int,input().split())

# 가장 작은 값을 출력한다.
d = ((a if (a<b) else b) if((a if (a<b) else b)<c) else c)
print(d)
