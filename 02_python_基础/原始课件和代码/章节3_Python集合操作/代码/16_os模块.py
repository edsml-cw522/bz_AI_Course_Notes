import os
# os.system('notepad.exe')
# os.system('ping www.baidu.com')

# cwd current working directory
print(os.getcwd())
my_working_directory = os.getcwd()
print(os.listdir(my_working_directory))

for x in os.listdir(my_working_directory):
    file_path = os.path.join(my_working_directory, x)
    # if os.path.isfile(file_path):
    if not os.path.isdir(file_path):
        print(file_path)

# os.chdir('D:/AIProject/pythonProject/test')
my_path = os.path.join(my_working_directory, 'test')
print(my_path)

if not os.path.exists(my_path):
    os.mkdir(my_path)

os.chdir(my_path)
print(os.getcwd())

# 批量重命名
for x in os.listdir(my_working_directory):
    file_path = os.path.join(my_working_directory, x)
    if os.path.isfile(file_path) and file_path.endswith(".py"):
        new_file_path = file_path.replace(' ', '')
        print(new_file_path)
        os.rename(file_path, new_file_path)