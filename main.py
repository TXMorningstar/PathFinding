'''
主程序范例
'''

from modules.autotrack import *

# 实例化Autotrack类
# "map"是可选参数，可以换成"raw"以及不填试试
track = Autotrack(64,64)

# 放置障碍物
track.obstacle((1,1))
track.obstacle((1,0))
track.obstacle((2,2))
track.obstacle((5,3))

# 寻路,把寻路结果赋值给一个变量
variable = track.target((0,0),(60,60))

# 打印路线
track.printTrack()  #打印一个好看的地图到cmd窗口上
print("Autotrack sucessed\n",variable) #在cmd窗口上打印寻路结果
