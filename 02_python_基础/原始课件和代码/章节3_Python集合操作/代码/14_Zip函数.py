
a = [10, 20, 30]
b = [40, 50, 60]
print(zip(a, b))
print(tuple(zip(a, b)))
print(tuple(zip(b, a)))
print(list(zip(a, b)))

a = [1, 2, 3]
b = ['我', '你', '他']
c = ['a', 'b', 'c']
print(list(zip(a, b, c)))
# print(dict(zip(a, b, c)))

zipped_list = list(zip(a, b, c))
# unzip
c, d, e = zip(*zipped_list)
print(c)
print(d)
print(e)

# 可以利用zip函数同时对多个长度相同的集合进行遍历
prog_langs = ['Python', 'Java', 'C', 'JavaScript']
features = [10, 20, 40, 30]
for lang, feature in zip(prog_langs, features):
    print(lang, feature)

# zip函数可以很好的和sorted函数结合使用
print(sorted(list(zip(features, prog_langs)), reverse=True))
