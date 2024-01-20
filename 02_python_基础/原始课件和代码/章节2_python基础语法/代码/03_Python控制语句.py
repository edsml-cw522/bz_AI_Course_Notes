uid = None

if uid == 0:
    print('root')

if uid is not None:
    print('uid is None')

# num = input("请输入一个整数：")
# print(type(num))
# if int(num) < 10:  # 获取的num是字符串，所以使用int()函数进行转换
#     print('您输入的整数是:', num)


if uid is None:
    print('root')
else:
    print('abc')

print('root') if uid is None else print('abc')

score = 87.8
level = int(score % 10)
print(level)
if level >= 10:
    print('Level A+')
elif level == 9:
    print('Level A')
elif level == 8:
    print('Level B')
elif level == 7:
    print('Level C')
elif level == 6:
    print('Level D')
else:
    print('Level E')
