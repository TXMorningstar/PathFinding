class AStarTrack(object):

    # 初始化类
    def __init__(self,x,y,print=None):
        self._x = x
        self._y = y
        self._print = print #print用于判断是否需要打印地图至cmd

        self._open = [] #open列表会记录所有被扫描过的点的坐标，这些坐标会被优先处理
        self._close = [] #close列表会记录所有已经计算过的点的坐标，这些坐标不会再被计算
        self._trace = [] #这个列表会在寻路完成后用于记录寻路结果

        # self.map与self._map的区别:
        # self.map是存储了地图大小以及障碍物信息的地图
        # self._map是用来计算的地图，计算后会重新初始化为self.map
        self.map = [[0 for i in range(y)] for i in range(x)]
        self._map = self.map

    '''
    地图相关的方法
    ----------------------------------------------------------------------------
    地图是一个二维列表，通过x和y可以访问到每一个坐标点。
    列表内0代表空格，没有障碍也没有角色
    列表中"o"代表障碍物(obstacle)，"e"代表终点(end)
    列表中被计算到的点会以元组的方式储存FGH以及父节点的值:
        (F的值,G的值,H的值,(父节点x,父节点y))
    '''

    # 传入一个turple作为坐标，将列表的对应坐标修改为障碍
    def obstacle(self,pos):
        self._map[pos[0]][pos[-1]] = "o"
        self.map = self._map

    # 返回地图的二维数组
    def getMap(self):
        return self.map

    # 以美观的方式打印地图
    def printMap(self):
        for x in range(self._y):
            for y in range(self._x):
                # 如果节点为开始坐标
                if (y,x) == self._start:
                    print("☆",end=" ")
                # 如果节点是结束坐标
                elif (y,x) == self._end:
                    print("★",end=" ")
                # 如果节点在open列表中
                elif (y,x) in self._open:
                    print("☑ ",end=" ")
                # 如果节点在close列表中
                elif (y,x) in self._close:
                    print("  ",end=" ")
                # 如果节点是障碍
                elif self.map[y][x] == "o":
                    print("■",end=" ")
                # 如果节点内数据为0
                else:
                    print("□",end=" ")
            print()

    # 适用于寻路完成后打印路线
    def printTrack(self):
        for x in range(self._y):
            for y in range(self._x):
                # 如果节点为开始坐标
                if (y,x) == self._start:
                    print("☆",end=" ")
                # 如果节点是结束坐标
                elif (y,x) == self._end:
                    print("★",end=" ")
                # 如果节点为路径之一
                elif (y,x) in self._trace:
                    print("• ",end=" ")
                # 如果节点是障碍
                elif self.map[y][x] == "o":
                    print("■",end=" ")
                # 如果节点内数据为0
                else:
                    print("□",end=" ")
            print()


    # 以程序的方式打印地图
    def printRawMap(self):
        for x in range(self._y):
            for y in range(self._x):
                print(self.map[y][x],end=" ")
            print()


    '''
    与寻路相关的方法
    ----------------------------------------------------------------------------
    实体是寻路的对象
    传入起点、终点即可寻路
    寻路时会以起点为中心向外寻路，绕开所有障碍物直到到达终点
    寻路完成后，返回前进的道路的每一步的坐标(turple)和总步数
    使用printTrack方法可以打印带有路径的地图
    '''
    def moveable(self,start,step):
        pass



    # 设定起点和终点
    #传入turple作为起始、结束坐标
    def target(self,start,end):
        # 将起始、结束坐标存入类属性中
        self._start = start
        self._end = end
        # 向地图中存放每一格的信息
        self.map[start[0]][start[-1]] = (self.attr(start,None),(start[0],start[1]))
        self.map[end[0]][end[-1]] = "e"
        # 把开始坐标放入open中以便寻路
        self._open.append(start)

        #开始寻路
        self.map = self._map #初始化地图
        self._open.clear()
        self._close.clear()
        self._trace.clear()
        minFpos = self.track()
        for i in range(self._x * self._y):
            minFpos = self.track(minFpos)
            if type(minFpos) == list:
                return minFpos

    # 计算F G H的值
    def attr(self,pos,father):
        # print("-----------------adding attr---------------------")
        # 初始化
        x = pos[0]
        y = pos[1]

        # G值计算 —— 移动步数
        # 如果是刚开始那一格那就不管他，步数只能是0
        if pos == self._start:
            g = 0
        else:
            g = self.map[father[0]][father[1]][0][1] + 1

        # H值计算 —— 终点的预估距离
        h = abs(pos[0]-self._end[0]) + abs(pos[1]-self._end[1])

        # F值计算 —— 移动优先值
        f = g + h

        # 返回F G H的值
        return (f,g,h)


    # 寻路
    # father代表父节点，子节点是由父节点衍生出的节点，父节点就是上一个被检查的节点
    def track(self,father=None):
        # 首先处理trace数据，如果trace不为空则证明寻路已完成。此时只需将trace数据向上抛回即可
        if self._trace:
            return self._trace

        # 取出节点
        # 首次运行时的初始化（如果没有父节点，说明这个节点是初次运行）
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
            # 检查一下有没有超出边界防止出现ListOutOfRange错误
            if x+i[0] >= 0 and y+i[1] >= 0 and x < self._x and y < self._y:
                scanpt = self.map[x+i[0]][y+i[1]] #scanpt会存储被扫描的点的数据

                # 被检查的点是否为路径终点
                if scanpt == "e":
                    return self.trace(father)
                # 判断:
                #   节点有无障碍、是否在close列表中
                #   现在还不是很清楚open列表是否需要检查，暂定为需要检查（跳过open列表可以减少部分计算量
                elif scanpt == 0 and scanpt not in self._close:
                    self._open.append((x+i[0],y+i[1])) #将节点信息放入open列表中
                    self.map[x+i[0]][y+i[1]] = (self.attr((x+i[0],y+i[1]),father),(father)) #向地图内添加F G H与父坐标的信息

        # 比对节点中F值最小的一个，这一个节点最有希望成为最短路径中的一个节点
        # 不过在开始比对之前还有一件事要做
        if len(self._open) == 0: #如果open列表里没有新的坐标了，说明无路可走了
            print("No matched way")
            return "fail"

        # 通过比对寻找子节点
        son = self.compare()

        # 现在可以打印地图了
        # print("-----------------tracking---------------------")
        if self._print == "raw":
            self.printRawMap()
            print("------------------------------------------------------------")
        if self._print == "map":
            self.printMap()
            print("------------------------------------------------------------")

        # 将节点从open中移至close
        self._open.remove(son) #把这个找到的坐标从open里移出去
        self._close.append(son) #然后把它加入到close列表中，以后不再判断

        # 继续迭代，检查下一个节点
        return son

    # 这个方法用于比对所有open中的节点并找出期望最优路径
    def compare(self):
        # 开始比对
        # comp会存放所有节点对应的F值，comp只是一个缓冲区，真正记录坐标的还是map、open和close
        # comp不必是一个字典，如果在循环内通过判断语句只把最低F值的坐标推进去的话也能达到一样的效果
        comp = self._open[0] #首先将第一个要比对的坐标放入comp完成初始化
        for i in range(len(self._open)):
            f = self.map[self._open[i][0]][self._open[i][1]][0][0] #找到F的值
            g = self.map[self._open[i][0]][self._open[i][1]][0][1] #找到G的值
            # 我们需要的最佳坐标，是F值最低的一个
            if f <= self.map[comp[0]][comp[1]][0][0]:
                # 但是如果有多个F值相等的坐标，则需要选择其中G值最低的坐标
                # H值无需计算，因为F值即为G与H之和，若G值相同，则H值毫无疑问也想通
                if f == self.map[comp[0]][comp[1]][0][0]:
                    if g < self.map[comp[0]][comp[1]][0][1]:
                        comp = self._open[i] #将坐标放进comp，格式是f:坐标
                else:
                    comp = self._open[i] #将坐标放进comp，格式是f:坐标
        # comp中存储的即为最优节点解
        return comp

    # 寻路到终点后，通过父坐标迭代返回并找到完整路径
    def trace(self,father):
        self._trace = [father,self._end] #终点的坐标一定是移动的最后一步，所以首先放入列表中；父坐标不会在循环内被输入列表，因此同样放入列表
        # 循环F次
        pos = father #正在检查的坐标，每检查一个新坐标就会更新一次

        # 如果路径过短会由于神秘力量报错，因此在循环前要进行判断
        if self.map[father[0]][father[1]][0][1] == 0:
            return [self._end]
        else:
            for i in range(self.map[father[0]][father[1]][0][1]):
                pos = self.map[pos[0]][pos[1]][1] #找到父节点，随后将下一个子节点更新为这个节点
                self._trace.append(pos) #把刚刚找到的父节点记录进trace里

            # 记录完成，接下来可以输出了
            self._trace.reverse() #因为append记录的列表是从终点向起点走过去的，因此需要反向列表
            return self._trace



# 这个类使用的是更新前的算法，需要遍历的路径更少，也就是寻路更快，但寻路的结果不一定精准
class BestFirstTrack(AStarTrack):

    def compare(self):
        # 开始比对
        comp = {} #comp会存放所有节点对应的F值
        for i in range(len(self._open)):
            f = self.map[self._open[i][0]][self._open[i][1]][0][0] #找到F的值
            comp[f] = self._open[i] #将坐标放进comp，格式是f:坐标
        return comp[min(comp)] #min(comp)通过字典找到了最低的f，然后以f作为key找到坐标，就算f有相同的也不影响
