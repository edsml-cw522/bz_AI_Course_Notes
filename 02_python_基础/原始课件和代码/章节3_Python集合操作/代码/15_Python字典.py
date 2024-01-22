a = {'name': 'baizhan', 'age': 18, 'job': 'programmer'}
print(a)

b = dict(name='baizhan', age=18, job='programmer')
print(b)

c = dict([('name', 'baizhan'), ('age', 18), ('job', 'programmer')])
print(c)

d = {}
e = dict()
print(d)
print(e)

a = [1, 2, 3]
b = ['我', '你', '他']
print(dict(zip(a, b)))

a = dict.fromkeys(['name', 'age', 'job'])
print(a)

# 修改字典
b = {'name':'baizhan', 'age':18, 'job':'programmer'}
b['address'] = 'beijing'
print(b)
b['age']=28
print(b)
a['name']='yasaka'
a['age']=18
a['job']='teacher'
print(a)

# 字典的访问
a = {'name':'baizhan', 'age':18, 'job':'programmer'}
print(a['name'], a['age'], a['job'])
# print(a['address'])

# get方法从字典中获取key对于的value;
# get方法的好处之一是，如果键不存在，返回None;
# get方法的好处之二是，可以设定指定键不存在的时候返回的值是多少;
# 推荐字典使用Get方法获取值
a = {'name':'baizhan', 'age':18, 'job':'programmer'}
print(a.get('name'))
print(a.get('age'))
print(a.get('job'))
print(a.get('address'))
print(a.get('address', 'beijing'))

a = {'name':'baizhan', 'age':18, 'job':'programmer'}
del a['name']
print(a)
b = a.pop('age')
print('age', b)
print(a)
a.clear()
print(a)

