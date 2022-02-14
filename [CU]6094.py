#방법 1
a = int(input())
b = map(int,input().split())
a = min(b)
print(a)

#방법 2
n = int(input())
a = input().split()

for i in range(n):           # a 배열 int 선언
    a[i] = int(a[i])

for i in range(n-1):         #a 배열에 있는 숫자들 비교
    if(a[i]<a[i+1]):         #앞에 칸이 뒤에 칸보다 작다면
         a[i+1] = a[i]       #앞에 칸 값을 뒤에 칸 값에 넣어준다
                             #만약, 앞에 칸이 뒤에 칸보다 크거나 같으면,그 값은 놔둔다.
print(a[n-1])                # 최종 남은 숫자가 마지막 배열 칸에 입력되있을때 이것을 출력
                
