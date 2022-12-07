# -*- coding:utf-8 -*-
# user:Liukang
from jsonpath import jsonpath
class Assert:
    @classmethod
    def assert_response(cls,assert_list:list,api_response:dict):
        # print(assert_list,api_response)
        new_assert_list=[]
        for i in assert_list:
            if '$.' in i:
                local=i.find('$')
                json_path=i[local:len(i)-1]
                value=jsonpath(api_response,json_path)
                if not value:
                    print('提取表达式失败，请检查')
                    return False
                value=str(value[0])
                i=i.replace(json_path,value)
            new_assert_list.append(i)
        print(f'断言新列表：{new_assert_list}')
        # 判断每个断言的成功或失败
        assert_result_list=[]
        for i in new_assert_list:
            assert_result=eval(i)
            print(f'断言表达式{i}，断言结果{assert_result}')
            assert_result_list.append(assert_result)
        # 断言结果列表有一个失败，断言失败
        if False in assert_result_list:
            return False
        return True

if __name__ == '__main__':
    api_response = {'msg': '请求成功','ig': '1'}
    assert_list = ["'1' == '$.ig'",' 2 == 1']
    print(Assert.assert_response(assert_list,api_response))
    res={'businessStatus': 1, 'message': 1, 'data': {'encryptedAccessToken': 'XbyEo0='}}
    lis=['"1" == "$.businessStatus"','"encryptedAccessToken" in "$.data"']
    print(Assert.assert_response(lis, res))