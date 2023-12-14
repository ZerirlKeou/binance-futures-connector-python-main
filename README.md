binance合约交易量化交易框架。此框架为策略编写框架，带有不同的回测和画图功能。

## 数据库
使用sqlite3数据库储存金融数据，其中包含了1m,5m,15m,1h,1d等不同时间级别的数据

## 绘图
感谢finplot提供的可交互式的金融绘图接口，相比于matplotlib绘图节省了大量的时间。其窗口的可交互性是本框架可视化的基础

## 回测
目前给出了简单的向量化回测的方法，不考虑交易的手续费以及滑点

## 时间级别训练数据的链接
对于时间级别的联立一般使用相邻的时间节点进行数据连接，目前尚未开发完整
