import argparse
import os
import shutil
import random

#运行命令
#python3 copyFile.py --count 2

def FindFile(path):
    for ipath in os.listdir(path):
        fulldir = os.path.join(path, ipath)  # 绝对路径
        # print(fulldir)  # 打印相关后缀的文件路径及名称
        if os.path.isfile(fulldir):
            shutil.copy(fulldir, new_path[random.randint(0, len(new_path)-1)])
        if os.path.isdir(fulldir):  # 目录，递归
            FindFile(fulldir)


def count_files_and_size(dir_path):
    # 初始化文件计算和文件大小计数
    file_count = 0
    total_size = 0

    # 遍历文件
    for root, dirs, files in os.walk(dir_path):
        # 遍历当前目录中的文件 
        for file in files:
            # 获取文件的完整路径
            file_path = os.path.join(root, file)
            # 获取文件大小以及检查它是否是一个文件 
            try:
                if os.path.isfile(file_path):
                    file_count += 1
                    total_size += os.path.getsize(file_path)
            except Exception as e:
                print(e)
                continue

    # 以元组的形式返回文件计数和总大小 
    return (file_count, total_size)

def printError(instr):
    return print("\033[31;1m{}\033[0m".format(instr))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # 调用add_argument方法添加参数
    parser.add_argument('--count', dest='count', default='1', type=int, help='输入对应参数')
    args = parser.parse_args()
    num = args.count

    new_path = ['/media/jetson/2A1B-77EB/202303301436/安全距离不足', '/media/jetson/2A1B-77EB/202303301436/PT损伤',
                '/media/jetson/2A1B-77EB/202303301436/PT脏污',
                '/media/jetson/2A1B-77EB/202303301436/导线断股', '/media/jetson/2A1B-77EB/202303301436/接头发热',
                '/media/jetson/2A1B-77EB/202303301436/金具损伤',
                '/media/jetson/2A1B-77EB/202303301436/金具锈蚀', '/media/jetson/2A1B-77EB/202303301436/绝缘子损伤',
                '/media/jetson/2A1B-77EB/202303301436/绝缘子污秽',
                '/media/jetson/2A1B-77EB/202303301436/无缺陷']

    # new_path = [r'C:\Users\11699\Desktop\图片\安全距离不足',r'C:\Users\11699\Desktop\图片\PT损伤',
    #             r'C:\Users\11699\Desktop\图片\PT脏污',
    #             r'C:\Users\11699\Desktop\图片\导线断股', r'C:\Users\11699\Desktop\图片\接头发热',
    #             r'C:\Users\11699\Desktop\图片\金具损伤',
    #             r'C:\Users\11699\Desktop\图片\金具锈蚀', r'C:\Users\11699\Desktop\图片\绝缘子损伤',
    #             r'C:\Users\11699\Desktop\图片\绝缘子污秽',
    #             r'C:\Users\11699\Desktop\图片\无缺陷']

    # new_path = [r'G:\新建文件夹 (2)\图片\安全距离不足',r'G:\新建文件夹 (2)\图片\PT损伤',
    #             r'G:\新建文件夹 (2)\图片\PT脏污',
    #             r'G:\新建文件夹 (2)\图片\导线断股', r'G:\新建文件夹 (2)\图片\接头发热',
    #             r'G:\新建文件夹 (2)\图片\金具损伤',
    #             r'G:\新建文件夹 (2)\图片\金具锈蚀', r'G:\新建文件夹 (2)\图片\绝缘子损伤',
    #             r'G:\新建文件夹 (2)\图片\绝缘子污秽',
    #             r'G:\新建文件夹 (2)\图片\无缺陷']

    old_path = '/media/jetson/2A1B-77EB/10kV商栗线'  # 要复制的文件所在目录
    # old_path = r'C:\Users\11699\Desktop\图片'  # 要复制的文件所在目录
    # 新路径
    folderList = []
    for i in range(0, num):
        for j in range(0, len(new_path)):
            os.makedirs(new_path[j] + str(i))
            new_path[j] = new_path[j] + str(i)
        print("new_path is ",new_path)
        folderList.append(new_path)
        FindFile(old_path)



    oldnum,oldsize, = count_files_and_size(old_path)
    print("原始路径是%s,原始路径下的文件数量: %d,原始路径下的文件总字节大小是: %d"%(old_path,oldnum,oldsize))

    newnum, newsize, = count_files_and_size("/media/jetson/2A1B-77EB/202303301436")
    if num*oldnum != newnum:
        printError("数量不一致，原始数量是：%d,新的数量是：%d"%(num*oldnum,newnum))
    if num*oldsize != newsize:
        printError("字节大小不一致，原始大小是：%d,新的大小是：%d" % (num*oldsize, newsize))

    print("测试结束，原始数量是：%d,新的数量是：%d；原始大小是：%d,新的大小是：%d"%(num*oldnum,newnum,num*oldsize, newsize))




