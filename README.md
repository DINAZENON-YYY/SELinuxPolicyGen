# SELinuxPolicyGen

## 数据结构

```
初始信息 先按照程序分析工具的格式来
{
  "name": "AprilFool",    //App名称
  "executor_label": "unconfined_t",   //启动该App的进程的上下文,先不管，可能需要ls -Z得到
  "public_file": {"/bin/bash":["x"], "/usr/share/alsa/alsa.conf":["w", "r"]},   //该App拥有的对公有目录的访问权限
  "private_file": {"/usr/bin/tests/testapp/app1/data":["d"], "data_file":["f"]}  //该App的私有目录及其类型（d为目录，f为文件),
}

type App struct {
	Name              string   // 包名
	Path              string   // app路径 暂定可能需要，先不用实现
	BinaryFiles       map[string][]string 二进制文件 暂定可能需要，先不用实现
	Executor_label:   string   //启动该App的进程的上下文,先不管，可能需要ls -Z得到,先不用实现
	SecurityLabel     string //主体标签
	SecurityExecLabel string //可执行文件标签
	SecurityDataLabel string //数据标签
	Public_file map<string,vector<string>> //访问公有文件 {"/bin/bash":["x"]}
	Private_file map<string,vector<string>>  //访问私有文件 {"/usr/bin/tests/testapp/app1/data":["d"]}
	PolicyPublicFile string //公有文件策略
	PolicyPrivateFile string //私有文件策略
	PolicyExecFile string //可执行文件策略
}

```



## 整体流程

```
DoAppPolicyGenerate(数据传入与预处理)  -> InitAppTypeDefine（type初始化）
	-> InitAppFilePolicy（文件allow）
	-> InitAppExcFilePolicy （可执行文件allow）
	-> MergePolicy
```



## py文件

```
main.py 读取文件信息
dataStruct.py 数据结构
policyGen.py 调用DoAppPlicyGenerate
se_process.py type初始化和查询系统默认type等
filePolicyGen.py 公有文件和私有文件的策略生成
execFilePolicyGen.py 可执行文件的策略生成
```

