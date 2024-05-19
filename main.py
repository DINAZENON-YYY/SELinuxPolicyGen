from policyGen import DoAppPolicyGenerate

test={'/var/log/message':{'read','write','open','execute'},'./hello':{'read'},'/etc/passwd':{'read','write'}}
name = 'test'
path='/home/user'

DoAppPolicyGenerate(name, path, test)