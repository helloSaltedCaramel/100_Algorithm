a,b = map(int,input().split())
a = bool(a)
b = bool(b)

#두 값의 True / False 값이 서로 다를 경우만 True 를 출력하고, 그 외의 경우에는 False 를 출력한다.
print(a and(not b) or (not a) and b)
