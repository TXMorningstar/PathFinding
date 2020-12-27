class Autotrack(object):

    '''
    初始化类
    ----------------------------------------------------------------------------
    传入一个实例化的类用于记录需要的数据
    如果要使用自动寻路，首先在外部创建一个类，并为类增加以下属性:

        必要参数:
            x           横向长度，类型应为int
            y           纵向长度，类型应为int

        若需要打印地图，需要这些参数:
            block       坐标中空格的样式，类型应为str
            start       起始坐标的样式，类型应为str
            end         目标坐标的样式，类型应为str
            obstacle    障碍物的样式，类型应为str
            track       路径的样式

        可以参考config.py中的设置
    '''
    def __init__(self,config):
        self.__config = config
        self.__open = []
        self.__close = []

        #创建映射表用于打印
        self._mappingtable = {
        0 : self.__config.block,
        "o" : self.__config.obstacle,
        "s" : self.__config.start,
        "e" : self.__config.end,
        "l" : self.__config.left,
        "r" : self.__config.right,
        "u" : self.__config.up,
        "d" : self.__config.down
        }


    '''
    地图相关的方法
    ----------------------------------------------------------------------------
    地图是一个二维列表，通过x和y可以访问到每一个坐标点。
    列表内0代表空格，没有障碍也没有角色
    列表中大于1的数字代表计算中的移动距离，每次寻路时都会使列表中的数字+1
    列表中"o"代表障碍物(obstacle)
    列表中"s"和"e"代表起点和终点(start)(end)
    '''
    # 创建地图
    def map(self,x,y):
        self._x, self._y = x, y
        self._map = [[0 for i in range(y)] for i in range(x)]

    # 传入一个turple作为坐标，将列表的对应坐标修改为障碍
    def obstacle(self,pos):
        self._map[pos[0]][pos[-1]] = "o"

    # 打印地图，默认不更新
    #与打印相关的方法可以用于快速调试和debug
    def printMap(self):

        for x in range(self._y):
            for y in range(self._x):
                # 如果坐标内为整型且不为0则正常输出
                if type(self._map[y][x]) == int and self._map[y][x] != 0:
                    print(self._map[y][x],end=" ")
                # 否则使用映射表输出
                else:
                    print(self._mappingtable[self._map[y][x]],end=" ")
            print()

    def printRawMap(self):
        for x in range(self._y):
            for y in range(self._x):
                print(self._map[y][x],end=" ")
            print()

    '''
    与寻路相关的方法
    ----------------------------------------------------------------------------
    实体是寻路的对象
    传入起点、终点和步数即可寻路
    寻路时会以起点为中心向外寻路，绕开所有障碍物直到到达终点
    寻路完成后，返回前进的道路的每一步的坐标(turple)和总步数
    使用printTrack方法可以打印带有路径的地图
    '''
    # 设定起点和终点
    #传入turple作为起始、结束坐标，step为最大寻路步数，默认为256
    def target(self,start,end,step=256):
        self._map[start[0]][start[-1]] = "s"
        self._map[end[0]][end[-1]] = "e"
        self._step = step
        self._start = start
        self._end = end

    # 寻路
    def track(self):
        def f(g,h):
            f = g + h
            return g+h

        def g(g):
            g += 1
            return g

        def h(start):
            return abs(start[0]-self._end[0]) + \
            abs(start[1]-self._end[1])


        x = self._start[0]
        y = self._start[1]
        for i in (0,-1),(-1,0),(0,1),(1,0):
            if self._map[x+i[0]][y+i[1]] != "o":
                # self._map[x+i[0]][y+i[1]] += 1
                print(self._map[x+i[0]][y+i[1]])
            else:
                print(self._map[x+i[0]][y+i[1]])


        # return self.track()

    # 打印路径
    def printTrack(self,sleep=False,time=0,update=False):
        pass

    # 操作方法
    # 命令控制
    def command(self):
        pass
