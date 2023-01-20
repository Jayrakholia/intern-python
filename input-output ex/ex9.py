import os

size = os.stat("E:\\Rejoice hub\\learn python\\input-output ex\\test.txt", "r").st_size
if size == 0:
    print('file is empty')
