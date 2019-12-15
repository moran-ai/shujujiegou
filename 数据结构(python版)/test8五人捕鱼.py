# def main():
'''fish = 1
while True:
    total = fish
    enough = True
    for _ in range(5):
        if (total - 1) % 5 == 0:
            total = (total - 1) // 5 * 4
        else:
            enough = False
            break
            if enough:
                print(f'总共有{fish}条鱼')
                break
            fish += 1'''

# if __name__ == '__main__':
#      main()

fish = 1
while 1:
    flag = 1
    total = fish
    for _ in range(5):  # _占位符，表示不在意变量的值，只是用于循环遍历N次，无法打印变量值
        if(total - 1)%5==0:  # % 取余
            total = (total - 1)// 5*4  # // 整除
        else:
            flag = 0
    if flag:
        print(fish)
        break
    fish += 1
