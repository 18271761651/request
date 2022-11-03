# -*- coding:utf-8 -*-
# user:Liukang

import os,yaml,random

class YamlUtil:

    # 读取yaml文件
    def read_extract_yaml(self):
        try:
            f = open(os.path.dirname(os.getcwd()) + '/extract.yml', 'r', encoding='utf8')
        except:
            f = open(os.getcwd() + '/extract.yml', 'r', encoding='utf8')
        finally:
            value = yaml.load(stream=f,Loader=yaml.FullLoader)
            f.close()
            return value;

    # 写入yaml文件
    def write_extract_yaml(self,data):
        try:
            f = open(os.path.dirname(os.getcwd()) + '/extract.yml', 'a', encoding='utf8')
        except:
            f = open(os.getcwd() + '/extract.yml', 'a', encoding='utf8')
        finally:
            value = yaml.dump(data=data,stream=f, allow_unicode=True)
            f.close()
            return value;

    # 清除
    def clear_extract_yaml(self):
        try:f=open(os.path.dirname(os.getcwd()) + '/extract.yml', 'w', encoding='utf8')
        except:f=open(os.getcwd() + '/extract.yml', 'w', encoding='utf8')
        finally:
            f.truncate()    # 清空内容
            f.close()       # 关闭文件

    # 读取测试用例yaml文件
    def read_testcase_yaml(self,yaml_name,**kwargs):
        try:f=open(os.path.dirname(os.getcwd()) + '/yaml_file/'+yaml_name, 'r', encoding='utf8')
        except:f=open(os.getcwd() + '/yaml_file/' + yaml_name, 'r', encoding='utf8')
        finally:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)  # 反序列化，将yaml文件变成字典格式 loader:加载方式
            f.close()
            return value;

if __name__ == '__main__':
    print(YamlUtil().read_testcase_yaml('test.yml'))