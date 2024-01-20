# for i in range(10):
#     if i==5:
#         break
#     print(i)
#
# names = ['Tom', 'Peter', 'Jerry', 'Jack']
# for i in range(len(names)):
#     if i>=2:
#         break
#     print(names[i])

for i in range(10):
    if i%2==0:
        continue
    print(i)

names = ['Tom', 'Peter', 'Jerry', 'Jack']
for i in range(len(names)):
    if i < 2:
        continue
    print(names[i])

while True:
    a = input("请输入一个字符（输入Q或q结束）")
    if a.upper()=='Q':
        print("循环结束，退出")
        break
    else:
        print(a)