import os

total_size=0
for root,dirs,files in os.walk(r'C:\Users\11699\Desktop\2'):
    for file in files:
        print(root+file)
        print(round(os.path.getsize(os.path.join(root,file))/1024/1024,2))
        total_size+=round(os.path.getsize(os.path.join(root,file))/1024/1024,2)
print(total_size)


password='测试一下输出'
name='名称'

print(f'正常输出：{password}，正常输出名字：{name}')