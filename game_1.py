#!/usr/bin/env python
#coding=utf-8
import random

readme='''
这是一个简单人机剪刀，石头，布的对战
请输入你的选择：
0 剪刀
1 石头
2 布
'''

choice_list = ['剪刀','石头','布']
win_list = ['剪刀布','石头剪刀','布石头']
times = 0
win_times = 0
while times < 3:
    player = choice_list[int(raw_input(readme))]
    computer = random.choice(choice_list)
    print '\n你选择了{you}，电脑选择了{computer}'.format(you=player,computer=computer)

    if player is computer:
        print 'no winner...'
    elif player + computer in win_list:
        print '\033[32mIN {} TIME,YOU WIN!!!\033[0m'.format(times+1)
        times += 1
        win_times += 1
    else:
        print '\033[31mIN {} TIME,YOU LOSE...\033[0m'.format(times+1)
        times += 1

if win_times >= 2:
    print '\n\033[32m############FINALLY,YOU WIN!!!###############\033[0m'
else:
    print '\n\033[31m############FINALLY,YOU LOSE!!!###############\033[0m'