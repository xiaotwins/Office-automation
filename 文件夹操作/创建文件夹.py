import os


def mkdir(path):
        folder = os.path.exists(path)
        if not folder:
            # os.mkdir(path)
            os.makedirs(path)  # 递归创建目录


for i in range(1, 5):
    path = f'temp/chapter{i}'
    mkdir(path)
