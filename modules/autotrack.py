class AutoTrack(object):
    def __init__(self,config):
        self.__config = config


    '''
    地图相关的方法

    地图是一个二维列表，通过x和y可以访问到每一个坐标点。
    列表内0代表空格，没有障碍也没有角色
    列表中大于1的数字代表计算中的移动距离，每次寻路时都会使列表中的数字+1
    列表中"block"代表障碍物
    列表中"start"和"destination"代表起点和终点
    '''
    # 创建地图
    def mapping(self,x,y):
        self._x, self._y = x, y
        self._map = [[0 for i in range(x)] for i in range(y)]

    # 传入一个turple作为坐标，将列表的对应坐标修改为障碍
    def obstacle(self,pos):
        self._map[pos[0]-1][pos[-1]-1] = "block"

    # 打印地图，默认不更新
    #这个方法可以用于debug
    def printMap(self,update=False):
        for x in range(self._x):
            for y in range(self._y):
                print(self._map[x][y],end="")
            print()

    '''
    与寻路相关的方法

    实体是寻路的对象
    '''
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
