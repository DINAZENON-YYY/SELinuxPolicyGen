"""

相关数据结构定义

"""
import os
from seProcess import findInDefault
class AppPolicyInfo:
    def __init__(self, name, path ,dic={}):  #dic为程序分析工具的输出
        self.name = name  # 包名
        self.security_label = ""  # 主体标签
        self.security_exec_label = ""  # 可执行文件标签
        self.security_data_label = ""  # 数据标签
        self.path = path  # app路径

        # 暂定可能需要，先不用实现
        self.binary_files = None  # 二进制文件
        self.executor_label = None  # 启动该App的进程的上下文

        # 访问公有文件和私有文件
        self.app_file = dic
        self.public_file = {}  # {"/bin/bash":["x"]}
        self.private_file = {}  # {"/usr/bin/tests/testapp/app1/data":["d"]}
        for key,value in dic.items():
            _,isok=findInDefault(key)
            if isok :
                self.public_file[key]=value
            else:
                isfile=os.path.isfile(key)
                if isfile:
                    self.private_file[key]=["f"]
                else:
                    self.private_file[key]=["d"]
        # 策略保存
        self.policy_public_file = []  # 公有文件策略
        self.policy_private_file = []  # 私有文件策略
        self.policy_exec_file = []  # 可执行文件策略
        self.policy_final = ""  # 最终安全策略

"""
dic={'/var/log/message':{'read','write','open',"execute"},'/hello':{'read'},'/etc/passwd':{'read','write'}}
a=AppPolicyInfo(name='test', path="/home/user", dic=dic)
print(a.public_file)
print(a.private_file)
"""

"""
{'/var/log/message': {'write', 'read', 'execute', 'open'}, '/etc/passwd': {'write', 'read'}}
{'/hello': ['d']}
"""
