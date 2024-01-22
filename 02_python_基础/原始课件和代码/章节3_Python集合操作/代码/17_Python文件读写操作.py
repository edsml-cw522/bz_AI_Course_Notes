
# f = open('test/text.txt', 'r', encoding='utf-8')
# data = f.read()
# print(data)
# f.close()

# f = open('test/text.txt', 'r', encoding='utf-8')
# data = f.readlines()
# print(data)
# f.close()

# f = open('test/text.txt', 'r', encoding='utf-8')
# line = f.readline()
# while line:
#     print(line)
#     line = f.readline()
# f.close()

# f = open('test/text.txt', 'w', encoding='utf-8')
# # f.write('让我们一起学习AI\n让我们一起学习Python')
# f.writelines(['让我们一起学习AI', '\n', '让我们一起学习Python'])
# f.close()

# f = open('test/text.txt', 'a', encoding='utf-8')
# f.write('\n')
# f.write('hello')
# f.close()

with open('test/text.txt', 'a', encoding='utf-8') as f:
    f.write(' ')
    f.write('world')
