'''
主程序范例
'''

from modules.autotrack import *
from config import *

config = Config()
game = Autotrack(config)

# 创建一个地图，传入大小、样式
game.map(config.x,config.y)
game.printMap()
game.obstacle((0,1))
game.obstacle((3,10))
print("-------------"*9)
game.printMap()
print("-------------"*9)
game.target((5,5),(10,10))
game.obstacle((5,6))
print("-------------"*9)
game.printMap()
game.track()
game.printRawMap()
