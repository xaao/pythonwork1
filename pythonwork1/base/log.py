import logging
import time
def llog():
    logger=logging.getLogger()
    logger.setLevel(logging.INFO)
    # 创建一个hander用于将日志写入文件
    rq=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
    log_filename='D:\\owner\\pywork\\pythonwork1\\\Logs\\'+rq+'.log'
    if not logger.handlers:
        fh=logging.FileHandler(log_filename,mode='a',encoding='utf-8')
        fh.setLevel(logging.INFO)
        # 创建一个hander用于输出到控制台
        ch=logging.StreamHandler()
        ch.setLevel(logging.INFO)
        # 定义handler的输出格式
        formeter=logging.Formatter('%(asctime)s-%(module)s-%(lineno)d-%(name)s-%(levelname)s-%(message)s')
        fh.setFormatter(formeter)
        ch.setFormatter(formeter)
        # 给logger添加handler
        logger.addHandler(fh)
        logger.addHandler(ch)
    return logger