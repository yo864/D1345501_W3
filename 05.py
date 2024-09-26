i = int(input('請輸入一個三位數:'))
n = int(i/100)
k = int((i-(n*100))/10)
j = int(i%10)
a = n
n = j
j = a
ans = n*100+j*10+k
print('結果:',ans)
