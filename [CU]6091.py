# 방법1
a,b,c = map(int,input().split())
day =1

while True:
  if day%a==0 and day%b==0 and day%c==0:
    print(day)
    break
  day +=1

#방법2
a, b, c = map(int, input().split())
day = 1

while (day%a!=0 or day%b!=0 or day%c!=0) :
  day += 1

print(day)
