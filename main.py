'''
主程序范例
'''

from modules.autotrack import *
from config import *

config = Config()
track = Autotrack(config)
printer = ShowMap(config)

# 创建一个地图，传入大小、样式
track.map(config.x,config.y)
track.obstacle((1,1))
track.target((0,0),(1,1))

# a = track.getMap()
# print("----------------\n"*20)
# print(a[0][0][0][1])

printer.printRawMap(track.getMap())

# printer.printMap(track.getMap())
