class AutoTrack(object):
    def __init__(self,config):
        __config = config


    #地图相关的方法
    # 初始化地图
    def mapInit(self,x,y):
        self._xSize, self._ySize = x, y

    # 创建地图
    def mapping(self):
        self.map = []

    # 添加障碍
    def obstacle(self,pos):
        pass

    # 打印地图，默认不更新
    def printMap(self,update=False):
        pass

    # 与实体相关的方法
    # 设定起点和终点
    def target(self,start,end):
        pass

    # 寻路
    def track(self):
        pass

    # 操作方法
    # 命令控制
    def command(self):
        pass
