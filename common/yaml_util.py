# -*- coding:utf-8 -*-
# user:Liukang

import os,yaml
from request.common.parameter_setting import ParametterSetting
class YamlUtil:
    # 读取yaml文件
    @classmethod
    def read_yaml(self,path):
        try: f = open(os.path.dirname(os.getcwd()) + path, 'r', encoding='utf8')
        except: f = open(os.getcwd() + path, 'r', encoding='utf8')
        finally:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            f.close()
            return value

    @classmethod
    def read_extract_yaml(self):
        return self.read_yaml('/extract.yml')

    # 写入yaml文件
    @classmethod
    def write_extract_yaml(self,data):
        try: f = open(os.path.dirname(os.getcwd()) + '/extract.yml', 'a', encoding='utf8')
        except: f = open(os.getcwd() + '/extract.yml', 'a', encoding='utf8')
        finally:
            value = yaml.dump(data=data,stream=f, allow_unicode=True)
            f.close()
            return value;

    # 清除
    @classmethod
    def clear_extract_yaml(self):
        try: f=open(os.path.dirname(os.getcwd()) + '/extract.yml', 'w', encoding='utf8')
        except: f=open(os.getcwd() + '/extract.yml', 'w', encoding='utf8')
        finally:
            f.truncate()    # 清空内容
            f.close()       # 关闭文件

    # 读取测试用例yaml文件
    @classmethod
    def read_testcase_yaml(cls,path):
        lis=[]
        for i in cls.read_yaml(path):
            # print(i)
            if i['is_run']:
                lis.append(i)
                if ParametterSetting.data_is_replace(i['request']['data']):
                    i['request']['data']=ParametterSetting.parameter_setting(i['request']['data'])
                yield i

    @classmethod
    def read_config_yaml(self):
        return self.read_yaml('/config/enviroment.yml')

if __name__ == '__main__':
    # print(os.path.abspath(os.getcwd()))
    i=YamlUtil.read_testcase_yaml('/yaml_file/login.yml')
    print(i)
    for l in i:
        print(l)
    # print(YamlUtil.read_config_yaml())
