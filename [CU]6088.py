#방법1
a,b,c = map(int,input().split())
for i in range(2,c+1):
    a +=b
print(a)                           #마지막 값을 출력
#방법2
a,b,c = map(int,input().split())
print(a+(b*(c-1)))
