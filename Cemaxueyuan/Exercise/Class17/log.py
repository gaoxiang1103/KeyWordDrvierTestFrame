import logging
# 封装日志用到三个组件：日志器、格式器、处理器

def TestLog():
    # 创建一个日志器，别的文件使用日志，就用到这个日志器
    logger = logging.getLogger()
    # 设置日志级别，打印日志时，会将对应级别以上的日志输出
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        # 创建一个格式器，通过设置日志格式，将输出的日志按照设置的格式进行输出
        fmt = '%(asctime)s %(levelname)s %(name)s %(filename)s %(funcName)s %(message)s'
        formater = logging.Formatter(fmt)

        # 创建一个处理器，可将日志信息输出到控制台或指定文件当中
        sh = logging.StreamHandler()
        logger.addHandler(sh)
        sh.setFormatter(formater)

        fh = logging.FileHandler('mylog.log', encoding='utf-8')
        logger.addHandler(fh)
        fh.setFormatter(formater)

    return logger
