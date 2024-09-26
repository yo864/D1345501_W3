import math
a = int(input('輸入係數a:'))
b = int(input('輸入係數b:'))
c = int(input('輸入係數c:'))
i = int(b**2-(4*a*c))
n = int(math.sqrt(i))
ans1 = float(-b+n)/(2*a)
ans2 = float(-b-n)/(2*a)
print('方程式的根為x1=',ans1,'x2=',ans2)