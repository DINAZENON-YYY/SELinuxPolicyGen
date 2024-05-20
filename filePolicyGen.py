"""

公有文件和私有文件 allow语句转换

"""
from dataStruct import AppPolicyInfo
import seProcess
import os
"""
(已实现)可以使用seProcess.findInDefault寻找默认type和判断公有私有
seProcess.findInDefault有两个返回值：type 和 ok。
当搜索到默认type时，type 为默认type，ok 为True
当未搜索到默认type时，type 为None，ok 为False
"""
def InitAppFilePolicy(app_policy_info : AppPolicyInfo):
    public_file=app_policy_info.public_file
    private_file=app_policy_info.private_file
    label=app_policy_info.security_label[0]
    label_perms={}
    file_perms={}
    for file , perms in public_file.items():
        type,isok=seProcess.findInDefault(file)
        if isok:
            for se_perm in perms :
                if type not in label_perms:
                    label_perms[type]={}
                    app_policy_info.security_label.append(type)
                label_perms[type][se_perm]=True
                file_perms[se_perm]=True
        else:
            print(f"{file}未找到相应的type")
    file_perm_slice=[]
    for file_perm in file_perms:
        file_perm_slice.append(file_perm)

    public_file_result = []
    private_file_result=[]
    formatted_string = "gen_require(`class file { %s };')" % " ".join(file_perm_slice)
    public_file_result.append(formatted_string)
    for file_type,se_perms in label_perms.items():
        public_file_result.append(f"gen_require(`type {file_type};')")
        se_perm_slice = [se_perm for se_perm in se_perms.keys()]
        permissions = " ".join(se_perm_slice)
        public_file_result.append(f"allow {label} {file_type}:file {{ {permissions} }};")

    for file,labels in private_file.items():
        is_dir=-1
        is_abs_path=os.path.isabs(file)
        for i in labels:
            if i == 'd':
                is_dir=1
            elif i == 'f':
                is_dir=0
        if not is_abs_path:
            file=app_policy_info.path.rstrip('/')+'/'+file
        se_file_type_flag=" "
        if is_dir == 1:
            se_file_type_flag="-d"
        elif is_dir ==0:
            se_file_type_flag="--"
        tmp=[]
        tmp.append(file)
        tmp.append(se_file_type_flag)
        tmp.append(f"gen_context(system_u:object_r:{app_policy_info.security_data_label[0]},s0)")
        private_file_result.append(tmp)
        app_policy_info.policy_public_file = public_file_result
        app_policy_info.policy_private_file = private_file_result
    return public_file_result,private_file_result


"""
#测试
dic={'/var/log/message':{'read','write','open'},'./hello':{'read'},'/etc/passwd':{'read','write'}}
app=AppPolicyInfo(name='test', path="/home/user", dic=dic)
a,b=InitAppFilePolicy(app)
print(a)
print(b)
"""

