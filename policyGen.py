from dataStruct import AppPolicyInfo
from filePolicyGen import InitAppFilePolicy
from execFilePolicyGen import InitAppExcFilePolicy
import seProcess

def InitAppTypeDefine():
    pass

def MergePolicy():

    pass

def DoAppPolicyGenerate(appname: str, appInfo: dict):
    "初始化"
    app_policy_info = AppPolicyInfo(appname)

    "简单标签处理"
    seProcess.simpleGenerateSecurityLabel(app_policy_info)
    seProcess.SimpleGenerateExecSecurityLabel(app_policy_info)
    seProcess.simpleGenerateDataSecurityLabel(app_policy_info)

    """先采用简单处理，这里先不用"""
    # InitAppTypeDefine()

    """普通文件allow语句转换"""
    InitAppFilePolicy()

    """可执行文件allow语句转换"""
    InitAppExcFilePolicy()

    """合并allow语句"""
    MergePolicy()
