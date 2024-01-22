# 创建元组
a = 1, 2, 3, 4, 5, 6, 7
print(type(a))

b = (1, 2, 3, 4, 5, 6, 7)
print(type(b))

c = (42,)
print(type(c))

d = ()
print(type(d))

a = tuple()
print(type(a))

a = tuple(('abc'))
print(a)

b = tuple(range(3))
print(b)

c = tuple([1, 2, 3, 4, 5])
print(c)

print(a)
print(a[1])
# a[1] = 20
# print(a[1])
# del a[1]

a = (20, 10, 30, 9, 8)
print(a[1])
print(a[1:3])
print(a[:4])

a = (20, 10, 30, 9, 8)
# a.sort()
print(sorted(a))
print(a)


