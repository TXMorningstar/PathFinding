from modules.autotrack import *
from config import *

config = Config()
game = AutoTrack(config)

# 创建一个地图，传入大小、样式
game.mapping(config.x,config.y)
game.printMap()
game.obstacle((2,10))
print("-------------"*9)
game.printMap()
print("-------------"*9)
