import logging
import os
import time

# DEBUG: 最低级别，追踪问题时使用
# INFO: 记录程序中一般事件的信息，或确认一切工作正常
# WARNING: 记录信息，用于警告
# ERROR: 用于记录程序报错信息
# CRITICAL: 最高级别，记录可能导致程序崩溃的错误

class Logging:
    @classmethod
    def make_log_dir(self,dirname='logs'):  # 创建存放日志的目录，并返回目录的路径
        now_dir = os.path.dirname(__file__) #返回上级目录basic
        father_path = os.path.split(now_dir)[0] #返回上上级目录pom
        path = os.path.join(father_path,dirname)
        path = os.path.normpath(path)
        if not os.path.exists(path):
            os.mkdir(path)
        return path


    def get_log_filename(self):         # 创建日志文件的文件名格式，便于区分每天的日志
        filename = "{}.log".format(time.strftime("%Y-%m-%d",time.localtime()))
        filename = os.path.join(self.make_log_dir(),filename)
        filename = os.path.normpath(filename)
        return filename

    @classmethod
    def loger(self,level='DEBUG'):      # 生成日志的主方法,传入对那些级别及以上的日志进行处理
        logger = logging.getLogger()    # 创建日志器
        level = getattr(logging,level)  # 获取日志模块的的级别对象属性
        logger.setLevel(level)          # 设置日志级别
        if not logger.handlers:         # 作用,防止重新生成处理器
            sh = logging.StreamHandler()# 创建控制台日志处理器
            fh = logging.FileHandler(filename=self.get_log_filename(self),mode='a',encoding="utf-8")    # 创建日志文件处理器
            # 创建格式器
            fmt = logging.Formatter("时间%(asctime)s，等级%(levelname)s，文件名%(filename)s，生成位置:%(lineno)d，信息:%(message)s")
            # 给处理器添加格式
            sh.setFormatter(fmt=fmt)
            fh.setFormatter(fmt=fmt)
            # 给日志器添加处理器，过滤器一般在工作中用的比较少，如果需要精确过滤，可以使用过滤器
            logger.addHandler(sh)
            logger.addHandler(fh)
        return logger   # 返回日志器

if __name__ == '__main__':
    logger = Logging.loger()
    logger.debug("1111111111111111111111") #使用日志器生成日志
    logger.info("222222222222222222222222")
    logger.error("附件为IP飞机外婆家二分IP文件放")
    logger.warning("3333333333333333333333333333")
    logger.critical("44444444444444444444444444")
