# -*- coding:utf-8 -*-
# user:Liukang

import os,yaml

class YamlUtil:

    # 读取yaml文件
    def read_extract_yaml(self):
        with open(os.path.dirname(os.getcwd())+'/extract.yml','r',encoding='utf8') as f:
            value = yaml.load(stream=f,Loader=yaml.FullLoader)
            return value;

    # 写入yaml文件
    def write_extract_yaml(self,data):
        with open(os.path.dirname(os.getcwd()) + '/extract.yml', 'a', encoding='utf8') as f:
            value = yaml.dump(data=data,stream=f, allow_unicode=True)
            return value;

    # 清除
    def clear_extract_yaml(self):
        with open(os.path.dirname(os.getcwd()) + '/extract.yml', 'w', encoding='utf8') as f:
            f.truncate()

if __name__ == '__main__':
    print(os.path.dirname(os.getcwd()))