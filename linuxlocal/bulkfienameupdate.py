
import os

def rename():
    i = 0
    path = "/home/deepaky/Desktop/update-folder/"
    for filename in os.listdir(path):
        print(filename)
        my_dest = "img" + str(i) + ".jpg"
        my_source = path + filename
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        i += 1

if __name__ == '__main__':
    rename()

#
# rename()
# path = "/home/deepaky/Desktop/update-folder/"
# print(os.listdir(path))