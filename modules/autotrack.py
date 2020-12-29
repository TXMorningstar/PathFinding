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
        self._map[start[0]][start[-1]] = (self.attr(start,None),(start[0],start[1]))
        self._map[end[0]][end[-1]] = "e"
        # 把开始坐标放入open中以便寻路
        self.__open.append(start)

        #开始寻路
        self.track()

    # 计算F G H的值
    def attr(self,pos,father):
        print("-----------------adding attr---------------------")
        # 初始化
        x = pos[0]
        y = pos[1]

        # G值计算 —— 移动步数
        # 如果是刚开始那一格那就不管他，步数只能是0
        if pos == self._start:
            g = 0
        else:
            g = self._map[father[0]][father[1]][0][1] + 1
        # H值计算 —— 终点的预估距离
        h = abs(pos[0]-self._end[0]) + abs(pos[1]-self._end[1])

        # F值计算 —— 移动优先值
        f = g + h

        # 返回F G H的值
        return (f,g,h)

    # 寻路
    # father代表父节点，子节点是由父节点衍生出的节点，父节点就是上一个被检查的节点
    def track(self,father=None):
        print("-----------------tracking---------------------")
        for x in range(self.__config.y):
            for y in range(self.__config.x):
                print(self._map[y][x],end=" ")
            print()







        # 首次运行时的初始化
        # 如果没有父节点，说明这个节点是初次运行
        if father == None:
            father = self._start
            x = self._start[0]
            y = self._start[1]
        # 否则就是第二次以后的运行了，这样的话就一定会有父节点
        else:
            x = father[0]
            y = father[1]


        # 扫描 “四个” 周边方块的信息，随后向坐标内保存F G H的值
        # 四个元组代表扫描的方向：上、左、下、右
        for i in (0,-1),(-1,0),(0,1),(1,0):
            scanpt = self.scan(x+i[0],y+i[1]) #scanpt会存储被扫描的点的信息

            # 判断:
            #   节点有无障碍、是否在close列表中
            #   现在还不是很清楚open列表是否需要检查，暂定为需要检查（跳过open列表可以减少部分计算量
            if scanpt == 0 and scanpt not in self.__close:
                self.__open.append((x+i[0],y+i[1])) #将节点信息放入open列表中
############### print("open =",self.__open)
                self._map[x+i[0]][y+i[1]] = (self.attr((x+i[0],y+i[1]),father),(father)) #向地图内添加F G H与父坐标的信息


        # 比对节点中F值最小的一个，这一个节点最有希望成为最短路径中的一个节点
        comp = {} #comp会存放所有节点对应的F值
        for i in range(len(self.__open)):
            f = self._map[self.__open[i][0]][self.__open[i][1]][0][0] #找到F的值
            comp[f] = self.__open[i] #将坐标放进comp，格式是f:坐标
        # 开始比对
        minFpos = comp[min(comp)] #min(comp)通过字典找到了最低的f，然后以f作为key找到坐标，就算f有相同的也不影响


        # 将节点从open中移至close
        self.__open.remove(minFpos) #把这个找到的坐标从open里移出去
        self.__close.append(minFpos) #然后把它加入到close列表中，以后不再判断

        # 继续迭代，检查下一个节点
        return self.track(minFpos)


    def scan(self,x,y):
        # 检查一下有没有超出边界，是不是障碍，如果是就不管了
        if x >= 0 and y >= 0 and self._map[x][y] != "b":
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
