'''
主程序范例
'''

from modules.autotrack import *

# 实例化Autotrack类
# "map"是可选参数，可以换成"raw"以及不填试试
track = Autotrack(16,16,"map")

# 放置障碍物
for i in (1,0),(1,1),(2,3),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(4,7),(3,7),(2,7),(1,7):
    track.obstacle(i)

# 寻路,把寻路结果赋值给一个变量
variable = track.target((0,0),(15,15))

# 打印路线
track.printTrack()  #打印一个好看的地图到cmd窗口上
print("Autotrack sucessed\n",variable) #在cmd窗口上打印寻路结果
