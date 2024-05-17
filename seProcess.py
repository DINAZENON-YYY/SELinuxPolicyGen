"""

相关数据处理

"""


from dataStruct import AppPolicyInfo

def simpleGenerateSecurityLabel(appPolicyInfo: AppPolicyInfo):
    appPolicyInfo.security_label = appPolicyInfo.name + "_t"

def SimpleGenerateExecSecurityLabel(appPolicyInfo: AppPolicyInfo):
    appPolicyInfo.security_exec_label = appPolicyInfo.name + "_exe_t"

def simpleGenerateDataSecurityLabel(appPolicyInfo: AppPolicyInfo):
    appPolicyInfo.security_data_label = appPolicyInfo.name + "_data_t"

"""寻找默认type也可以判断是否为公有还是私有，待完善"""
def findInDefault(fileName : str):
    fileVector = []
    return None, False
    if fileName in fileVector:
        return fileVector[fileName], True
    else:
        return None, False