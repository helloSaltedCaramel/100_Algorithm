h,b,c,s = map(int,input().split())
store = float(h*b*c*s) 
print(format(store/8/1024/1024,'.1f'),'MB')
