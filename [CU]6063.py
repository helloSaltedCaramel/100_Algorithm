a,b = map(int,input().split())

#a와 b를 정수형으로 입력받은 뒤 c는 a>=b일 때 a이고, 이외에는 b라는 3항 연산
c = (a if (a>=b) else b)
print(c)
