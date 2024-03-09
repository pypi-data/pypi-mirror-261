# --coding:UTF-8-- #
#Code by LeonMMcoset
'''
This is Leon Random Plus,that add more functions to the random!
To use it,code "import leonranp"

Copyright LeonMMcoset.All rights reserved.
'''
#Code Running Info Start
print('-------------Leon Random Plus-------------')
print('You are using Leon Random Plus')
print('PyPI:https://pypi.org/project/leonranp/')
print('Wiki:http://leonmmcoset.jjmm.ink:8002/doku.php?id=leonranp')
print('To upgrade,use "upgrade()" on your shell')
print('To have help,use "lrphelp()"')
print('------------------------------------------')
#Code Running Info End
from random import *
from os import *
#Start Code#
#randstr:just code "randstr()".
def randstr():
    randstrlist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    randstr = choice(randstrlist)
    print(randstr)
#randcode:if you want to print code,code "print(randcode())"
#The randcode() values can be assigned in variables.
#To print randcode,code "print(randcode())"
def rcrandstr():
    randstrlist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    rcrandstr = choice(randstrlist)
    return rcrandstr
def randcode(hmuch):
    randcode = ''
    for i in range(hmuch):
        if randint(0,1)==0:
            randcode = randcode + str(randint(0,9))
        else:
            randcode = randcode + str(rcrandstr())
    return randcode
#randbool:if you want to print on,code "randbool()"
#The randbool() values can be assigned in variables.
def randbool():
    randbool = randint(0,1)
    return bool(randbool)
#End Code#
#Start Upgrade Code(use "upgrade()" to upgrade Leon Random Plus)
def upgrade():
    package_name = 'requests'
    system(f'pip install --upgrade leonranp')
#End Upgrade Code
#You can use "leonranp.help()" to get help!
def lrphelp():
    print('---Leon Random Plus Help Start---')
    print('randstr() -> Random string')
    print('randcode(hmuch) -> Random code(such as print a675a or 687dsa or 7s8 and more).')
    print('upgrade() -> Upgrade Leon Random Plus')
    print('randbool() -> Random bool')
    print('---Leon Random Plus Help End---')