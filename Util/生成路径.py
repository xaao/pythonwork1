import os
import shutil

for i in range(0,200):
    fulldir='C:\\Users\\11699\\Desktop\\1\\0'+str(i)
    os.makedirs(fulldir)
    shutil.copy(r'C:\Users\11699\Desktop\1\10kV宝度233线毕村支线#20211109-607.jpg', fulldir)

