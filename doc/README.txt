一 综述

系统分为后台和前端两部分，统一由nigix代理
80端口为 web端口 90端口为后台端口 具体看dev/niginx.conf
因为目前他主要是做前台展示，不需要访问后台数据接口


二 后台

后台部署在阿里云，目前一个实例，快过期了

nigix + gunicorn + django + django rest framework + postgres

后台管理 使用supervisoid

后台部署步骤：
ssh root@47.93.237.94 (password hfy@19891112)
cd miracle-server
3. . /dev/pipline.sh 拉取github,安装插件，数据库更新，收集静态文件
4.(可选）supervisord -c dev/supervisord.conf
5. supervisorctl -c dev/supervisord.conf 进入supervisor CLI
6. restart miracle
7.(可选) 更新nigix.conf, 重启nigix

后台目录说明
/dev 部署相关文件
/accounts 用户
/flowers 花模型
/logs 日志
/media 上传文件目录
/miracle_server 项目主目录，用于配置
/weixin weixin接口

代码地址：https://github.com/zhaoyudong0129/miracle-serve

三 前端
前台架构采用 angular 2
代码地址：https://github.com/zhaoyudong0129/miracle-web
1.安装 node,npm
2 安装 angular-cli
3 npm install 安装包依赖

具体看angluar 2 文档，采用angular-cli脚手架 