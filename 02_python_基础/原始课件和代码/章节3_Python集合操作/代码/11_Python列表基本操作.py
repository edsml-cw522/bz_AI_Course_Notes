# 列表中添加元素
a = [10, 20, 30]
a.append(40)
print('增加元素后的列表：', a)

a = [10, 20, 30]
b = [40, 50]
print(a + b)

a = [10, 20, 30]
b = [40, 50]
a.extend(b)
print(a)

# 使用insert函数插入元素
a = [10, 20, 30]
a.insert(2, 100)  # 在列表a的索引2处插入元素100
print(a)

a = [10, 20, 30, 40, 50, 20, 30, 20, 30]
print(a.index(20))  # 从列表中搜索第一个20
print(a.index(20, 3))  # 从索引位置3开始往后搜索的第一个20

a = [10, 20, 30, 40, 50, 20, 30, 20, 30]
a[1] = 5000
print(a)
del a[1]
print(a)
# del a
# print(a)

a = [1, 2, 3, 4, 5, 6]
b = a.pop()  # 没有指定位置，默认的是最后一个元素
print(b)
print(a)
c = a.pop(2)  # 删除下标为2的元素
print(c)
print(a)

a = [10, 20, 30, 40, 50, 20, 30, 20, 30]
a.remove(20)
print(a)
# a.remove(100)              #没有100这个元素，会抛出异常

a = ['sxt', 100]
b = a * 3
print(a)
print(b)

# b=['a',30,'b',40]
# print(max(b))       #字符串和数字不能比较，将抛出异常

# count()统计元素出现的次数
a = [10, 20, 40, 30, 10, 20, 50, 10]
print('元素10出现的次数：', a.count(10))
print('元素20出现的次数：', a.count(20))
print('元素30出现的次数：', a.count(30))

while a.count(20) > 0:
    a.remove(20)
print(a)

# sort()用于对列表进行排序，调用该方法会改变原来的列表
a = [11, 20, 13, 34, 5, 36, 17]
a.sort()
print(a)
print('正序：', a)
a.sort(reverse=True)
print('逆序：', a)

# sorted用于对列表进行排序，生成新列表，不改变原来的列表
print('-' * 5, 'sorted排序', '-' * 5)
a = [11, 20, 13, 34, 5, 36, 17]
b = sorted(a)
print('a列表：', a)  # 原来列表不会被修改
print('正序b列表：', b)
