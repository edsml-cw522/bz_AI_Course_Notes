# 创建

aList = []
print(type(aList))

aList = [2,3,1,1,2,3,'a string']
print(aList)

aList = list()
print(type(aList))

print(type((2,3,1,1,2,3,'a string')))
aList = list((2,3,1,1,2,3,'a string'))
print(type(aList))

aList = list(range(3, -10, -1))
print(type(aList))
print(aList)

# 列表生成式
aList = [x for x in 'abcdefg']
print(aList)

aList = []
for x in 'abcdefg':
    aList.append(x)
print(aList)

aList = [x*2 for x in range(1,5)]
print(aList)

aList = [x*2 for x in range(1,20) if x%5==0 ]
print(aList)

aList = []
for x in range(1,20):
    if x%5==0:
        aList.append(x*2)
print(aList)