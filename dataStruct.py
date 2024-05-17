"""

相关数据结构定义

"""

class AppPolicyInfo:
    def __init__(self, name):
        self.name = name  # 包名
        self.security_label = ""  # 主体标签
        self.security_exec_label = ""  # 可执行文件标签
        self.security_data_label = ""  # 数据标签

        # 暂定可能需要，先不用实现
        self.path = None  # app路径
        self.binary_files = None  # 二进制文件
        self.executor_label = None  # 启动该App的进程的上下文

        # 访问公有文件和私有文件
        self.public_file = {}  # {"/bin/bash":["x"]}
        self.private_file = {}  # {"/usr/bin/tests/testapp/app1/data":["d"]}

        # 策略保存
        self.policy_public_file = ""  # 公有文件策略
        self.policy_private_file = ""  # 私有文件策略
        self.policy_exec_file = ""  # 可执行文件策略
        self.policy_final = ""  # 最终安全策略
