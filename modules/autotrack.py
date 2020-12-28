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

    '''
    地图相关的方法
    ----------------------------------------------------------------------------
    地图是一个二维列表，通过x和y可以访问到每一个坐标点。
    列表内0代表空格，没有障碍也没有角色
    列表中"o"代表障碍物(obstacle)，"e"代表终点(end)
    列表中被计算到的点会以元组的方式储存FGH以及父节点的值:
        (F的值,G的值,H的值,(父节点x,父节点y))
    '''
    # 创建地图
    def map(self,x,y):
        self._x, self._y = x, y
        self._map = [[0 for i in range(y)] for i in range(x)]

    # 传入一个turple作为坐标，将列表的对应坐标修改为障碍
    def obstacle(self,pos):
        self._map[pos[0]][pos[-1]] = "o"

    # 返回地图的二维数组
    def getMap(self):
        return self._map

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
    #传入turple作为起始、结束坐标
    def target(self,start,end):
        # 将起始、结束坐标存入类属性中
        self._start = start
        self._end = end
        # 向地图中存放每一格的信息
        self._map[start[0]][start[-1]] = (self.attr(start),(start[0],start[1]))
        self._map[end[0]][end[-1]] = "e"


    def test(self,pos):
        x = pos[0]
        y = pos[1]
        print("test------------------------------",self._map[x][y])####################################################################用这个方法测试就会发现问题




    # 计算F G H的值
    def attr(self,pos):
        print("-----------------here we go---------------------")
        # 初始化
        x = pos[0]
        y = pos[1]

        # G值计算 —— 移动步数
        # if self._map[pos[0]][pos[1]] == 0:
        # 如果是刚开始那一格那就不管他，步数只能是0
        if pos == self._start:
            g = 0
        else:
            g = self._map[x][y] + 1#[0][1]
            print("g=%s---------------"%self._map[x][y])###############################################这里出bug了

        # H值计算 —— 终点的预估距离
        h = abs(x-self._end[0]) + abs(y-self._end[1])

        # F值计算 —— 移动优先值
        f = g + h

        # 返回F G H的值
        return (f,g,h)

    # 寻路
    def track(self,father = None):
        # 初始化
        if father == None:
            father = self._start
            x = self._start[0]
            y = self._start[1]

        # 取出 “一个” 节点

        # 扫描 “四个” 周边方块的信息
        for i in (0,-1),(-1,0),(0,1),(1,0):
            scanpt = self.scan(x+i[0],y+i[1])

            # 判断:
            #   节点有无障碍、是否在open列表中，是否在close列表中
            if scanpt == 0 and scanpt not in self.__close:
                self.__open.append((x+i[0],y+i[1]))
                print(self.__open)
                self._map[x+i[0]][y+i[1]] = (self.attr((x+i[0],y+i[1])),(father))
            else:
                print(self._map[x+i[0]][y+i[1]])


        # 关闭节点


    def scan(self,x,y):
        # 首先检查一下有没有超出边界，超出了就不管它
        if x >= 0 and y >= 0:
            return self._map[x][y]





    # 操作方法
    # 命令控制
    def command(self):
        pass


class ShowMap(object):
    def __init__(self,config):
        self.__config = config

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

    # 以美观的方式打印地图
    def printMap(self,map):
        for x in range(self.__config.y):
            for y in range(self.__config.x):
                # 如果坐标内为整型且不为0则正常输出
                if type(map[y][x]) == int and map[y][x] != 0:
                    print(map[y][x],end=" ")
                # 否则使用映射表输出
                else:
                    print(self._mappingtable[map[y][x]],end=" ")
            print()

    # 以程序的方式打印地图
    def printRawMap(self,map):
        for x in range(self.__config.y):
            for y in range(self.__config.x):
                print(map[y][x],end=" ")
            print()
