# -*- coding:utf-8 -*-
# user:Liukang
import os

#定义文件目录
result_dir = os.path.dirname(os.path.dirname(__file__)) + '/test_report/'
#获取目录下所有文件
lists = os.listdir(result_dir)
#重新按时间对目录下的文件进行排序
lists.sort(key=lambda fn: os.path.getatime(result_dir+'\\'+fn))

print("最新的文件为："+lists[-1])  #lists[-1]取最新生成的文件
file = os.path.join(result_dir, lists[-1])
print(file)		#打印路径和文件
