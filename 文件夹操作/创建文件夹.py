import os


def mkdir(path):
        folder = os.path.exists(path)
        if not folder:
            os.mkdir(path)


for i in range(2, 10):
    path = f'D:\File\GitHub\Data-analysis-and-Application\chapter{i}'
    mkdir(path)
