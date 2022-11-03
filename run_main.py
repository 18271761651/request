import os,pytest,allure

if __name__ == '__main__':
    pytest.main(['-vs','-m=smoke','--alluredir','./reports/tmp'])
    os.system('allure generate ./reports/tmp -c -o ./reports/html' )

    # pytest常用命令：
        # -x:用例运行失败则立即停止执行
        # -s:运行过程中执行print打印函数
        # --collect-only或--co:收集将要执行的用例，但不会执行用例
        # -v/--verbose或-q/--quiet:打印用例执行的详细或简略过程
        # -k args（args可以是py文件名，也可以是函数名）运行包含关键词的用例
        # pytest --html=path 生成简易html报告，path是存储报告的路径。
        # --alluredir = DIR：在指定目录DIR生成allure报告
        # --clean - alluredir：清除alluredir如果目录存在的化
        # 一般结合 - -alluredir = DIR命令一起使用 如：pytest --alluredir=./report/html --clean-alluredir
        # --maxfail=num 用例运行时 允许的最大失败次数，超过则立即停止
        # -m 'mark1 and not mark2'
        # --markers显示所有mark标记，用例运行带有mark1标记的并且不运行mark2标记的
        # --tb = 选项（选项：'auto', 'long', 'short', 'no', 'line', 'native'）用例运行失败时，展示错误的详细程度
        # -l或--showlocals用例运行失败时，打印相关的局部变量，pytest - l
        # --lf, --last - failed    只执行上次执行失败的测试
        # --ff, --failed - first先执行完上次失败的测试后，再执行上次正常的测试
        # 运行指定的函数（使用两对冒号: 分隔）pytest 模块名::类名::函数名，pytest test.py::check_ui

    # Allure常用命令：
        # commond: generate 生成allure报告
        # 示例：
        # allure
        # generate. / report / xlm - o. / report / html - c. / report / html
        # 在生成新的Allure报告之前，先清除该目录： `-c, --clean`
        # 指定目录生成allure报告： `-o, --report - dir, --output`

        # commond：open 打开生成的报告，本地查看生成的报告，本地查看
        # 示例：
        # allure
        # open. / report / html
        # 指定域名地址：-h, --host
        # 指定端口号：-p, --port

        # commond：serve 打开生成的报告，可对外提供在线展示
        # 示例：
        # allure
        # serve. / report / html
        # 指定域名地址：-h, --host
        # 指定端口号：-p, --port

    # Allure执行命令
        # 选择运行你要执行epic的用例
        # pytest - -alluredir. / report / allure - -allure - epics = epic
        # 选择运行你要执行features的用例
        # pytest - -alluredir. / report / allure - -allure - features = 模块名称
        # 选择运行你要执行features的用例
        # pytest - -alluredir. / report / allure - -allure - stories = 子模块名称

    # Allure常用函数
        # 使用方法                  含义                    使用说明
        # @allure.epic()          史诗，可以理解为背景介绍    敏捷里面的概念，下一级是story
        # @allure.feature()       功能模块名称              功能模块的描述，下一级是story
        # @allure.story()         用户故事                 故事描述，下一级是是title
        # @allure.title()         用例标题                报告中的用例名称，若不写，默认方法名
        # @allure.testcase()      用例链接地址              对应测试用例系统里面的case
        # @allure.issue()         缺陷地址                对应缺陷管理系统里面的链接
        # @allure.description()   用例描述                测试用例的描述
        # @allure.step()          操作步骤                测试用例的步骤
        # @allure.severity()      用例等级                五种等级：blocker，critical，normal，minor，trivial
        # @allure.link()          链接                    定义一个链接，在测试报告展现
        # @allure.attachment()    附件                    在报告中添加附件