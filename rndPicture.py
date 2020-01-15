import os, random
from flask import url_for

def get_random_picture():
    #1-считаем список названий файлов .jpg из папки pic
    dir = 'static'
    files = os.listdir(dir)
    images = filter(lambda x: x.endswith('.jpg'), files)
    images = list(images)
    #2-выбрать случайным образом название файла
    return random.choice(images)

if __name__=="__main__":
    f = get_random_picture()
    print(f)