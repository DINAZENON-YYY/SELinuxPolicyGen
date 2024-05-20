from dataStruct import AppPolicyInfo
def simpleGenerateSecurityLabel(appPolicyInfo: AppPolicyInfo):
    appPolicyInfo.security_label.append(appPolicyInfo.name + "_t")

def SimpleGenerateExecSecurityLabel(appPolicyInfo: AppPolicyInfo):
    appPolicyInfo.security_exec_label.append(appPolicyInfo.name + "_exe_t")

def simpleGenerateDataSecurityLabel(appPolicyInfo: AppPolicyInfo):
    appPolicyInfo.security_data_label.append(appPolicyInfo.name + "_data_t")