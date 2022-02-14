#방법1
a = int(input())
total = 0

i =1

while (total < a):
    total += i
    i += 1
print(total)

#방법 2
a = int(input())
s = 0
c = 0
while True: 
    s += c
    c += 1
    if s >=a:
        break
print(s)
