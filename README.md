# zhiyunIOT

#### 介绍
智云家居是为用户调试、连接、控制物联设备所开发的一款智能物联网平台。智云家居由前端、后端，及Mqtt消息服务器，硬件共同组成。安卓端具备添加设备，控制设备，广播配网，web配网，查看在线设备数量。

智云家居前端由Android studio开发，部分view、Adapter均是独立开发

后端接口主要由python flask （现在正在向Java web过度）实现，接口与数据库连接由pyMysql实现。


#### 安装教程

1.  服务器运行智云后端.py (python 智云后端.py)
2.  打包Android app
3.  部署mqtt服务器

#### 接口说明

1. "/"根路由，测服务器是否正常运行
2.  "/zt"查询设备在线数量及状态
3.  "/rgb"RGB设备调试接口
4.  "/dn"控制布尔设备状态
5.  "/additme"向数据库添加设备
6.  "/addview"向数据库添加view
7.  "/cxview"查询数据库view
8.  "/myjjjj"名言警句接口
9.  "/vieod"视频图传接口

