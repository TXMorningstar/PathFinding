'''
主程序范例
'''

from modules.autotrack import *
from config import *

config = Config() #实例化Config类
track = Autotrack(config) #实例化Autotrack类，传入config类的实例


track.map(config.x,config.y) #创建一个地图，传入大小、样式
track.obstacle((1,1)) #放置一个障碍物
print(track.target((0,0),(10,10))) #寻路，然后打印寻路结果
