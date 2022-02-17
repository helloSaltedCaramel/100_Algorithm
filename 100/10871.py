# x보자 작은 수
a,x = map(int,input().split())
num = list(map(int,input().split()))
for i in range(a):
    if num[i]<x:
        print(num[i], end=' ')
        
# for 문을 이용해서 range(n), n=10이므로 i 는 0부터 9까지 입력된다. 
# 그리고 들여쓰기 후 if 문을 이용해서 num[0~9] list에 있는 숫자들이 x인 5보다 작을 떄 print 함수를 이용해서 출력하게 된다.
