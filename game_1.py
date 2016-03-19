#!/usr/bin/env python
#coding=utf-8
readme='''这是一个简单人机剪刀，石头，布的对战
请输入你的选择：
1 剪刀
2 石头
3 布

'''
import random
choice_list=['剪刀','石头','布']
win_list=['剪刀布','石头剪刀','布石头']
player=choice_list[int(raw_input(readme))]
computer=random.choice(choice_list)

if player is computer:
    print 'no winner...'
elif player + computer in win_list:
    print '\033[32mYOU WIN!!!\033[0m'
else:
    print '\033[31mYOU LOSE...\033[0m'
