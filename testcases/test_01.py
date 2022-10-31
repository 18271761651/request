import pytest,allure,requests,pprint,random,string
from requests_toolbelt import MultipartEncoder
from request.common.log import Logging
from request.common.yaml_util import YamlUtil

@allure.feature("测试类名")
class TestRequest:

    Authorization=''

    def setup(self):
        print('\n每个用例前执行')

    def teardown(self):
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

    def my_callback(self,monitor):
        progress = (monitor.bytes_read / monitor.len) * 100
        print("\r 文件上传进度：%d%%(%d/%d)" % (progress, monitor.bytes_read, monitor.len), end=" ")

    @allure.story("登录")
    def test_login(self):
        '''登陆'''
        url = 'http://116.63.186.61:2031/api/Common/Login/Login'
        headers = {'Content-Type': 'application/json'}
        data = {
          "loginName": "hlcs",  # 登录名
          "pwd": "123456",      # 密码
          "expirationDays": 1   # 有效天数
        }
        r = requests.post(url, headers=headers, json=data,allow_redirects=False)
        self.print(r)
        YamlUtil().write_extract_yaml({"Authorization":("Bearer "+r.json()['data']['encryptedAccessToken'])})
        assert 'encryptedAccessToken' in r.text

    @allure.story("上传文件")
    def test_upload(self,conn_database):
        '''图片上传'''
        url='http://116.63.186.61:2031/api/Common/Files/Upload'
        headers=YamlUtil().read_extract_yaml()
        file={
            'module': 'Goods',
            'Files': ('弥豆子.jpg', open('E:\图片\Saved Pictures\鬼灭之刃.jpg','rb'), 'image.png')
        }
        # 因为16位数随机的，每次都不一样
        boundary = '----WebKitFormBoundary' \
                   + ''.join(random.sample(string.ascii_letters + string.digits, 16))

        data = MultipartEncoder(fields=file, boundary=boundary)
        headers["Content-Type"] = data.content_type
        # '''添加监听器'''
        # data_2=MultipartEncoderMonitor(data_1, self.my_callback)
        r = requests.post(url=url, headers=headers, data=data,allow_redirects=False)
        assert r.json()['businessStatus']==1
        self.print(r)

    @pytest.mark.smoke
    def test_03(self):
        pass

    @pytest.mark.smoke
    def test_04(self):
        pass

    def test_05(self):
        pass
if __name__ == '__main__':
    # os.system('pip install -r requirements.txt')
    # pytest.main(['-s', '-q', '--alluredir', './report/xml'])
    # pytest.main(['-s', '-q', 'test_01.py', '--clean-alluredir', '--alluredir=../allure/allure-results'])
    # os.system(r"allure generate -c -o ../reports/allure-report")    # -c:清空历史数据 -o:指定输出测试报告路径
    # os.system(r'allure serve ../allure/allure-results') # 在默认浏览器中显示生成的报告

    pytest.main() #['-vs','-n=2','--reruns=2','--html=../reports/report.html']


