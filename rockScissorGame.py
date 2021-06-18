# -*- coding: utf-8 -*- 

import random
human = int(input('가위  1 , 바위 2, 보  3 중 하나를 선택해봐'))
if human not in [1,2,3]:
    raise Exception('가위 바위 보 중 하나 입력해!')
computer = random.randint(1,3)
diff = human - computer

if(diff==-1 or diff==2): 
    print("컴퓨터가 낸 것 :")
    print('너가 졌어 ㅠ 내가 이겼다 ㅎ')
if(diff==1 or diff==-2):
    print('헐,,, 너가 이김;; 최고b')
if(diff==0): 
    print('비겼다! 유셈셈')
