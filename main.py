'''
主程序范例
'''

from autotrack import *

track = AStarTrack(16,16,"map") #实例化AStarTrack类
# track = AStarTrack(16,16,"raw")
# track = AStarTrack(16,16)
# track = BestFirstTrack(16,16."map")

# 放置障碍物
for i in (1,0),(1,1),(2,3),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(4,7),(3,7),(2,7),(1,7),(0,7):
    track.obstacle(i)

# 寻路,把寻路结果赋值给一个变量
variable = track.target((0,0),(15,15))
track.printTrack()  #打印一个好看的地图到cmd窗口上
print("---------------------------------------")
track.target((4,4),(9,9))

# 打印路线
track.printTrack()  #打印一个好看的地图到cmd窗口上
# print("Trace found\n",variable) #在cmd窗口上打印寻路结果


# 实现反复寻路的方法有两个：
#     第一个方法可以解决短期中的问题，但是可维护性不足，同时效率较慢：
#         每次寻路完成后重新生成地图，然后传入障碍物数据
#     第二个方法可以解决长期问题，且较为稳定：
#         self._map只用于存储地图和障碍，所有寻路计算都用局部变量中的地图进行计算
#     第三个方法是创建两个地图，第一个地图用于记录障碍和地图全局；第二个地图用于计算与寻路
