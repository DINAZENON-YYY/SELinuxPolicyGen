from policyGen import DoAppPolicyGenerate

name = 'test'
test={
    '/var/log/message':{'read','write','open'},
    './hello':{'read'},
    '/etc/passwd':{'read','write'},
    "/usr/bin/emerge":{'execute'}}
path='/home/user/test'

DoAppPolicyGenerate(name, path, test)