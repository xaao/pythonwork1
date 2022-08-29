import yaml

from base.log import llog
logger=llog()

class Getdata:
    def get(self,path):
        logger.info('获取yaml文件数据')
        file=open(path,'r',encoding='utf-8')
        data=yaml.load(file,yaml.FullLoader)
        return data
