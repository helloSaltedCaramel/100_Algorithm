
# 정수 2개를 공백으로 구분해 입력
# 각각 정수형으로 만들어준다.
a,b = map(int,input().split())

# a 를 2^b만큼 곱한 값을 구하고 출력한다
print(a<<b)
