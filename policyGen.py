from dataStruct import AppPolicyInfo
from filePolicyGen import InitAppFilePolicy
from execFilePolicyGen import InitAppExcFilePolicy
from labelProcess import simpleGenerateDataSecurityLabel
from labelProcess import simpleGenerateSecurityLabel
from labelProcess import SimpleGenerateExecSecurityLabel

def InitAppTypeDefine():
    pass

def MergePolicy(app_policy_info : AppPolicyInfo):
    policy_type_file = [app_policy_info.security_label, app_policy_info.security_exec_label, app_policy_info.security_data_label]

    policy_type = "type " + app_policy_info.security_label + '\n'
    policy_public = ""
    policy_private = ""
    policy_exec = ""

    if app_policy_info.policy_exec_file:
        policy_type += "type " + app_policy_info.security_exec_label + '\n'

    for public_file in app_policy_info.policy_public_file:
        policy_public += "\n" + public_file + "\n"

    for private_file in app_policy_info.policy_private_file:
        final_private = ""
        for private_item in private_file:
            final_private += private_item + "   "
        policy_private += "\n" + final_private + "\n"

    for exec_file in app_policy_info.policy_exec_file:
        policy_exec += "\n" + exec_file + "\n"

    te_file = policy_type + policy_public
    # print(te_file)
    fc_file = policy_private + policy_exec

    with open(app_policy_info.name + "_t" + ".te", 'w', encoding="UTF-8") as f:
        f.write(te_file)

    with open(app_policy_info.name + "_t" + ".fc", 'w', encoding="UTF-8") as f:
        f.write(fc_file)


def DoAppPolicyGenerate(appname: str, apppath : str, appInfo: dict):
    "初始化"
    app_policy_info = AppPolicyInfo(appname, apppath, appInfo)

    "简单标签处理"
    simpleGenerateSecurityLabel(app_policy_info)
    SimpleGenerateExecSecurityLabel(app_policy_info)
    simpleGenerateDataSecurityLabel(app_policy_info)

    """先采用简单处理，这里先不用"""
    # InitAppTypeDefine()

    """普通文件allow语句转换"""
    InitAppFilePolicy(app_policy_info)
    # print(app_policy_info.policy_public_file)
    # print(app_policy_info.policy_public_file)
    print("file Complete")
    """可执行文件allow语句转换"""
    InitAppExcFilePolicy(app_policy_info)
    print(app_policy_info.policy_exec_file)
    print("exec Complete")
    """合并allow语句"""
    MergePolicy(app_policy_info)
    print("Merge Complete")

