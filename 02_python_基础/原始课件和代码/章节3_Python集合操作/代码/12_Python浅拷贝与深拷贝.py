'''
# 直接赋值
a = [11, 22, 33]
b = a
print(b)
# print(id(a), id(b))
print(a is b)
print(a == b)

c = {'name': 'baizhan'}
d = c
# print(id(c), id(d))
print(c is d)
print(c == d)

a.append(44)
print(a)
print(b)
print(a is b)
print(a == b)

c['age'] = 21
print(c)
print(d)
print(a is b)
print(a == b)


# 浅拷贝
a = [1, 2]
b = [3, 4]
c = [a, b]
d = c
# print(c is d)
# print(c == d)

import copy
e = copy.copy(c)
# print(id(c), id(d), id(e))
print(c is d)
print(c == d)
print(e is c)
print(e == c)

print(c[0] is d[0])
print(c[0] is e[0])

a.append(5)
b.append(6)
print(c)
print(d)
print(e)
'''
import copy

# 深拷贝
a = [1, 2]
b = [3, 4]
c = [a, b]
d = copy.deepcopy(c)
print(c is d)
print(c[0] is d[0])
print(c[1] is d[1])

c.append(5)
print(c)
print(d)

a.append(3)
b.append(5)
print(c)
print(d)

d[0].append(5)
d[1].append(6)
print(d)
print(c)

d.append(7)
print(d)
print(c)
