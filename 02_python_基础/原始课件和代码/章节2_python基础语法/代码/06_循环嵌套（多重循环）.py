# 打印九九乘法表

j = 1
while j <= 9:
    i = 1
    while i <= j:
        print("%d*%d=%d" % (j, i, i * j), end='\t')
        i += 1
    print()
    j += 1


for j in range(1, 10):
    for i in range(1, j+1):
        print("%d*%d=%d" % (j, i, i * j), end='\t')
    print()
