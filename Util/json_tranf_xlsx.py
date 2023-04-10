import json
import jsonpath
import xlwt
import os

# 需要提前安装库
# 使用方法：将origin_path替换成本地的路径直接执行
#
def Getdata(paths,filenames):
    for i in range(0,len(filenames)):
        path=paths[i]
        filename=filenames[i]
        worksheet = workbook.add_sheet(filename)
        lis=['time','job_cpu_usage_seconds_total','time','job_memory_working_set_bytes','time','job_network_receive_bytes_total','time','job_network_transmit_bytes_total']
        for i in range(8):
            worksheet.write(0,i,lis[i])
        json_data = json.load(open(path,'r',encoding='utf8'))
        rank=0
        for i in [0,2,3,4]:
            values_list=jsonpath.jsonpath(json_data,f'$.data.result[{i}].values')
            row=1
            for value in values_list[0]:
                worksheet.write(row,rank, value[0])
                worksheet.write(row,rank+1, value[1])
                row+=1
            rank+=2

if __name__ == '__main__':
    origin_path='C:\\Users\\11699\\Desktop\\333333'
    paths,filenames=[],[]
    for root, dirs, files in os.walk(origin_path):
        for file in files:
            paths.append(os.path.join(root,file))
            filenames.append(file)
        print(paths,filenames)
    workbook = xlwt.Workbook(encoding='ascii')
    Getdata(paths,filenames)
    workbook.save(f'{origin_path}\\数据.xlsx')  # 保存文件

