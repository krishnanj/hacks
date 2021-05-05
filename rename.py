## rename multiple files in a directory with prefix

import os

fmt = ".png"
cwd = os.getcwd() + '/'

print(cwd)

for i, filename in enumerate(os.listdir(cwd)):
    os.rename(cwd + filename, "prefix" + str(i) + fmt)