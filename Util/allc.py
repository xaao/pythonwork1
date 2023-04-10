import argparse
import pynvml
import psutil
import time

#计算gpu使用百分比
def getGpu():
    # print(meminfo.free/1024**2)  #剩余显存大小（float）
    # print(pynvml.nvmlDeviceGetCount())#显示有几块GPU
        pynvml.nvmlInit()
        handle = pynvml.nvmlDeviceGetHandleByIndex(0) # 指定显卡号
        meminfo = pynvml.nvmlDeviceGetMemoryInfo(handle)
        totalGpu=meminfo.total/1024**2 #总的显存大小（float）
        usedGpu=meminfo.used/1024**2  #已用显存大小（float）
        return round((usedGpu/totalGpu*100),2)
        # return 1
# 计算内存、磁盘、cpu百分比
def getAccl():
    mem = psutil.virtual_memory()
    totalmem = float(mem.total) / 1024 / 1024 / 1024 # 系统总计内存
    usedmem = float(mem.used) / 1024 / 1024 / 1024 # 系统已经使用内存
    return str(round((usedmem / totalmem * 100), 2)) + ',' + str(psutil.cpu_percent(1)) + ',' + str(psutil.disk_usage('/').percent)

if __name__ == '__main__':
    print("开始时间是:{}".format(time.strftime("%Y-%m-%d %H:%M:%S")))
    parser = argparse.ArgumentParser()
    # 调用add_argument方法添加参数
    parser.add_argument('--count', dest='count', default='8', type=int, help='输入对应参数')
    args = parser.parse_args()
    num=(args.count)*60*60
    b=1
    with open('ceshi.txt', 'w') as a:
        a.write('gpu,mem,cpu,disk'+'\n')
    while num>b:
        with open('ceshi.txt', 'a') as a:
            a.write(str(getGpu())+','+getAccl()+'\n')
        num=num-b
        time.sleep(1)
    print("结束时间是:{}".format(time.strftime("%Y-%m-%d %H:%M:%S")))