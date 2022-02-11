#방법 1
x = int(input())
result = 0

for i in range(1, x+1):
  result += i
  if result >= x :
    print(i)
    break
  
#방법 2
a = int(input())
sum = 0
count = 0
while(sum<a):
    count += 1
    sum += count
print(count)
