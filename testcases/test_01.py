import json
import re

import pytest,allure,requests,pprint,random,string,os
from requests_toolbelt import MultipartEncoder
from request.common.yaml_util import YamlUtil
from request.common.request_util import ReuqestsUtil
from request.common.log import Logging
from request.common.case import case_assert_result

@allure.feature("测试类名")
class TestRequest:

    def setup_method(self):
        print('\n每个用例前执行')

    def teardown_method(self):
        print('\n每个用例后执行')

    def print(self,response):
        print('状态码：',response.status_code)
        print('\n响应头',)
        pprint.pprint(response.headers)
        print('\n响应体')
        pprint.pprint(response.json())
        print('\n请求头')
        pprint.pprint(response.request.headers)
        print('\n请求体')
        pprint.pprint(response.request.body)

    # def my_callback(self,monitor):
    #     progress = (monitor.bytes_read / monitor.len) * 100
    #     print("\r 文件上传进度：%d%%(%d/%d)" % (progress, monitor.bytes_read, monitor.len), end=" ")

    @allure.story("登录")
    @pytest.mark.parametrize('caseinfo',YamlUtil().read_testcase_yaml('/yaml_file/login.yml'))
    def test_login(self,caseinfo,conn_database):
        '''登陆'''
        method=caseinfo['request']['method']
        api = caseinfo['request']['api']
        data = caseinfo['request']['data']
        Logging.loger("INFO").info(f'API:{api},请求类型：{method},请求参数{data}')
        r = ReuqestsUtil().send_request(method=method,api=api, json=data)
        YamlUtil().write_extract_yaml({"Authorization":("Bearer "+r.json()['data']['encryptedAccessToken'])})
        assert 'encryptedAccessToken' in r.text
        # assert case_assert_result(caseinfo)

    @allure.story("上传文件")
    @pytest.mark.parametrize('caseinfo',YamlUtil().read_testcase_yaml('/yaml_file/upload.yml'))
    def test_upload(self,caseinfo,conn_database):
        f'''{caseinfo['name']}'''
        headers=YamlUtil().read_extract_yaml()
        api = caseinfo['request']['api']
        method = caseinfo['request']['method']
        module=caseinfo['request']['data']['module']
        filename=caseinfo['request']['data']['filename']
        filepath=caseinfo['request']['data']['filepath']
        formate=caseinfo['request']['data']['formate']
        file={
            'module': module,
            'Files': (filename, filepath, formate)
        }
        # 因为16位数随机的，每次都不一样
        boundary = '----WebKitFormBoundary' \
                   + ''.join(random.sample(string.ascii_letters + string.digits, 16))

        data = MultipartEncoder(fields=file, boundary=boundary)
        headers["Content-Type"] = data.content_type
        # '''添加监听器'''
        # data_2=MultipartEncoderMonitor(data_1, self.my_callback)
        r = ReuqestsUtil().send_request(method=method,api=api, headers=headers, data=data)
        assert r.json()['businessStatus']==1
        # self.print(r)

    @pytest.mark.smoke
    def test_03(self,conn_database):
        pass

    @pytest.mark.smoke
    def test_04(self):
        pass

    def test_05(self):
        pass

if __name__ == '__main__':
    # os.system('pip install -r requirements.txt')
    # pytest.main(['-s', '-q', 'test_01.py', '--clean-alluredir', '--alluredir=../result/allure-results'])
    # os.system(r'allure serve ../result/allure-results') # 在默认浏览器中显示生成的报告

    # pytest.main(['-vs','test_01.py','-m=parametrize','--alluredir','../reports/tmp']) #['-vs','-n=2','--reruns=2','--html=../reports/report.html']
    # os.system(r"allure generate ../reports/tmp -c -o ../reports/html")    # -c:清空历史数据 -o:指定输出测试报告路径
    pytest.main(['-vs','test_01.py::TestRequest::test_login'])

