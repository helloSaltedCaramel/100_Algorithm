a = int(input())
num = a 
count = 0
while True:
    sum_num = (num//10)+(num%10)
    new_num = ((num % 10)*10)+(sum_num%10)
    count += 1
    if new_num == a:
        break
    num = new_num 
print(count)
