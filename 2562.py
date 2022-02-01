_max = 0
idx = -1 
for i in range(1,10):
    a = int(input())
    if a> _max: 
        _max = a
        idx = i
print(_max)
print(idx)
