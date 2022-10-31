import os,time
import pytest,allure,requests,pprint,random,string
from requests_toolbelt import MultipartEncoder,MultipartEncoderMonitor

@allure.feature("测试类名")
class TestRequest:
    Authorization=''
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
        url = 'http://116.63.186.61:2031/api/Common/Login/Login'
        headers = {'Content-Type': 'application/json'}
        data = {
          "loginName": "hlcs",  # 登录名
          "pwd": "123456",      # 密码
          "expirationDays": 1   # 有效天数
        }
        r = requests.post(url, headers=headers, json=data,allow_redirects=False)
        # self.print(r)
        self.Authorization = "Bearer "+r.json()['data']['encryptedAccessToken']

    @allure.story("上传文件")
    def test_upload(self):
        '''图片上传'''
        url='http://116.63.186.61:2031/api/Common/Files/Upload'
        headers={'Authorization': self.Authorization}

        file={
            'module': 'Goods',
            'Files': ('弥豆子.jpg', open('E:/Picture/wallpaper/弥豆子.jpg','rb'), 'image.png')
        }
        # 因为16位数随机的，每次都不一样
        boundary = '----WebKitFormBoundary' \
                   + ''.join(random.sample(string.ascii_letters + string.digits, 16))

        data_1 = MultipartEncoder(fields=file, boundary=boundary)
        headers["Content-Type"] = data_1.content_type
        # '''添加监听器'''
        # data_2=MultipartEncoderMonitor(data_1, self.my_callback)
        r = requests.post(url=url, headers=headers, data=data_1,allow_redirects=False)
        # self.print(r)


if __name__ == '__main__':
    # pytest.main(['-s', '-q', '--alluredir', './report/xml'])
    pytest.main(['-s', '-q', 'test_01.py', '--clean-alluredir', '--alluredir=../allure/allure-results'])
    # os.system(r"allure generate -c -o ../reports/allure-report")    # -c:清空历史数据 -o:指定输出测试报告路径
    os.system(r'allure serve ./allure-results') # 在默认浏览器中显示生成的报告
    # pytest.main(['-–html=./report.html','test_01.py'])
