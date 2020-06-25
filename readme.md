## 自用简易图床

目前没有任何安全措施

### 食用方法

* 需要python, flask, pymysql, mysql 环境

* 在mysql 下创建账户，数据库，数据库中表的格式可在 DataBase.py 中找到

* 将web.py 中host, port, name, password, database_name 填全

* 运行web.py

* 默认端口为7000

#### 上传方式

可以在/upload中手动点按钮上传

也可以在/upload中使用post上传

* 头部  dataType: "text"  contentType: false

* 参数为 file 为要上传的图片

* 返回值 字符串 表示图片的相对位置 如 /upload/14342

#### 实现简介

暴力把图片放在了mysql中

没有考虑安全，性能和美观，停留在了能用的阶段~~