from modules.autotrack import *
from config import *

config = Config()
game = AutoTrack(config)

# 创建一个地图，传入大小、样式
game.mapInit(config.x,config.y,config.block,config.entity,config.destination,config.track,config.obstacle)
game.mapping()
game.printMap()
