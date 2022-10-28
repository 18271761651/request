import os,pytest,unittest

cur_path = os.path.dirname(__file__)

def add_case(caseName='case',rule='test_01.py'):
    case_path = os.path.join(cur_path,caseName)
    if not  os.path.exists(case_path):
        os.mkdir(case_path)
    print(case_path)
    discover=unittest.defaultTestLoader.discover(case_path,
                                                 pattern=rule)
    print(discover)
    return discover
if __name__ == '__main__':
    add_case()