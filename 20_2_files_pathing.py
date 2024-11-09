import os
print(os.getcwd()) # Путь текущей директории
print(os.listdir()) # все файлы текущей директории

# новая папка
# cwd = os.getcwd()
# new_dir = 'test'
# path = os.path.join(cwd, new_dir) # генерируем путь до новой папки
# os.mkdir(path) # создаем новую папку
# print(os.listdir())

# копирование файлов
# import shutil
# path = r'test/temp1.txt' # Во что копируем
# file = r'file.txt' # Что копируем
# copy_file = shutil.copy(file, path)

#Копирование папки
# import shutil
# path = r'/Users/stronberry/PycharmProjects/QAP-175/module 20/' # откуда = содержимое какой папки
# new_path = r'/Users/stronberry/PycharmProjects/QAP-175/module 20/test/' # куда (если существует = удаление и перезапись)
# Remove the target directory if it already exists
# if os.path.exists(new_path):
#     shutil.rmtree(new_path)
# # Copy the directory
# copy_dir = shutil.copytree(path, new_path)

# #Перемещение файлов
# import shutil
# path = r'/Users/stronberry/PycharmProjects/QAP-175/module 20/test/' #куда
# file = r'/Users/stronberry/PycharmProjects/QAP-175/module 20/python.txt' #что
# dir = shutil.move(file, path)

# #Для удаления директории вместе со всеми файлами используют shutil.rmtree():
# import shutil
# path = r'C:\Users\Liudmila\Python\test'
# shutil.rmtree(path)
#
# # Для удаления файлов используют метод os.remove():
# import os
# path = r'C:\Users\Liudmila\Python\file.txt'
# os.remove(path)