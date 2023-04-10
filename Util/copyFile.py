import argparse
import os
import shutil
import random


def FindFile(path):
    for ipath in os.listdir(path):
        fulldir = os.path.join(path, ipath)  # 绝对路径
        # print(fulldir)  # 打印相关后缀的文件路径及名称
        if os.path.isfile(fulldir):
            shutil.copy(fulldir, new_path[random.randint(0, len(new_path)-1)])
        if os.path.isdir(fulldir):  # 目录，递归
            FindFile(fulldir)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # 调用add_argument方法添加参数
    parser.add_argument('--count', dest='count', default='1', type=int, help='输入对应参数')
    args = parser.parse_args()
    num = args.count

    new_path = ['/media/qaz/202303301436/安全距离不足','/media/qaz/202303301436/PT损伤',
                '/media/qaz/202303301436/PT脏污',
                '/media/qaz/202303301436/导线断股', '/media/qaz/202303301436/接头发热',
                '/media/qaz/202303301436/金具损伤',
                '/media/qaz/202303301436/金具锈蚀', '/media/qaz/202303301436/绝缘子损伤',
                '/media/qaz/202303301436/绝缘子污秽',
                '/media/qaz/202303301436/无缺陷']

    # new_path = [r'C:\Users\11699\Desktop\图片\安全距离不足',r'C:\Users\11699\Desktop\图片\PT损伤',
    #             r'C:\Users\11699\Desktop\图片\PT脏污',
    #             r'C:\Users\11699\Desktop\图片\导线断股', r'C:\Users\11699\Desktop\图片\接头发热',
    #             r'C:\Users\11699\Desktop\图片\金具损伤',
    #             r'C:\Users\11699\Desktop\图片\金具锈蚀', r'C:\Users\11699\Desktop\图片\绝缘子损伤',
    #             r'C:\Users\11699\Desktop\图片\绝缘子污秽',
    #             r'C:\Users\11699\Desktop\图片\无缺陷']

    old_path = '/media/qaz/500picture'  # 要复制的文件所在目录
    # old_path = r'C:\Users\11699\Desktop\图片'  # 要复制的文件所在目录
 # 新路径
    for i in range(0,num):
        for j in range(0,len(new_path)):
            os.makedirs(new_path[j]+str(i))
            new_path[j]=new_path[j]+str(i)
        print(new_path)
        FindFile(old_path)