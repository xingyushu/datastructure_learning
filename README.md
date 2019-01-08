# coding
coding 是一套基于七牛实时音视频、七牛直播云实现的在线代码教学平台。

## 1. 系统架构图

![系统架构](http://ozuriq73f.bkt.clouddn.com/WechatIMG49.jpeg)

## 2. 数据库模型设计


#### 项目介绍
后端使用 beego+mgo 开发 

#### 软件架构
软件架构说待补充


#### 参与开发

```bash
$ mkdir -p $GOPATH/src/gitee.com/talcoding
$ cd $GOPATH/src/gitee.com/talcoding
$ git clone git@gitee.com:talcoding/coding.git
$ cd coding
$ go run main.go

```

#### 特别说明

* 采用不忽略 vendor 目录的机制，后期可能会忽略
* 采用新分支的方式提交 pr