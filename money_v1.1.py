#!usr/bin/env python
#coding:utf-8

import time
import os
import cPickle
def add_money():
    mount = int(raw_input('请输入你要存的金额:'))
    content = raw_input('描述:')
    date = time.strftime('%Y%m%d')
    with open('wallet') as f:
        money = cPickle.load(f) + mount
    with open('wallet','w') as f:
        cPickle.dump(money,f)
    with open('record','a') as f:
        f.write('%-10s%-10s%-10s%-10s%-20s\n' %(date, 'N/A', mount, money, content))



def spend_money():
    mount = int(raw_input('请输入你要存的金额:'))
    content = raw_input('描述:')
    date = time.strftime('%Y%m%d')
    with open('wallet') as f:
        money = cPickle.load(f) - mount
    with open('wallet', 'w') as f:
        cPickle.dump(money, f)
    with open('record', 'a') as f:
        f.write('%-10s%-10s%-10s%-10s%-20s\n' %(date, 'N/A', mount, money, content))

def select_money():
    with open('record') as f:
        for line in f:
            print line,
    with open('wallet') as f:
        print '\033[32mNow money is {}\033[0m'.format(cPickle.load(f))



if __name__ == '__main__':
    if not os.path.isfile('wallet'):
        with open('wallet', 'w') as f:
            cPickle.dump(1000, f)
    if not os.path.isfile('record'):
        with open('record', 'w') as f:
            f.write('%-10s%-10s%-10s%-10s%-20s\n' %('date', 'spend', 'add', 'money', 'describe'))
    cmds = {'0':add_money, '1':spend_money,'2':select_money}
    while True:
        readme = '''(0)存钱
(1)消费
(2)查询
(3)退出
请选择[0|1|2|3]中的一个数字:'''
        choice = raw_input(readme).strip()[0]

        if choice not in '0123':
            print 'error'
        elif choice == '3':
            break
        else:
            cmds[choice]()
