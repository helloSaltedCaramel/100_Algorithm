#방법 1
a = int(input(),16)
for i in range(1,16):
    print('%X*%X=%X'%(a,i,a*i))
 
#방법 2
a = int(input(), 16)   #16진수로 받기
for i in range(1,16):
  print('%X'%a,'*%X'%i, '=%X' %(a*i), sep='')   # print('%X'%n): n에 저장되어있는 값을 16진수 형태로 출력하겠다
