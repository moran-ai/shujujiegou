'''# 1到10000之内的自守数
for  i in range(10000):
    if i*i%(10**(len(str(i)))) ==i:  # 如果i的平方数的尾数等于i本身
       print(i)
       '''

'''
# 出售金鱼算法
n = 11
while True:
    x = n
    for i in range(2, 5+1):
        x = x-(x/i+1/i)
    if x == 11:
        print(n)
        #####
        x = n
        for i in range(2, 5+1):
            m = x/i+1/i
            x = x - m
            print('%d: mai-->%d shend-->%d' %(i-1, m, x))
        #####
        break
    n = n + 1'''
'''
# 借书算法
count = 0
for a in range(1,6):
    for b in range(1,6):
        if a!= b:
            for c in range(1,6):
                if c!=b and c!=a:
                   count += 1
                   print(count)
'''

