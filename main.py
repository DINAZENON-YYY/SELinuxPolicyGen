from policyGen import DoAppPolicyGenerate

test={'/var/log/message':{'read','write','open'},'./hello':{'read'},'/etc/passwd':{'read','write'},"/usr/bin/emerge":{'execute'}}
name = 'test'
path='/home/user'

DoAppPolicyGenerate(name, path, test)