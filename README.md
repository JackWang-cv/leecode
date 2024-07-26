# leecode
# 6月，7月: 二分+贪心
# git知识
    远程仓库名称指的是你的代码仓库存储的位置，可以是 origin、github、gitee 等。
    分支名称指的是你在代码仓库中的工作线，可以是 main、master 等。
    git remote -v 查看远程仓库
    git remote add yyy xxx yyy为远程仓库名可自定义，xxx为https形式或者ssh, 用于gitee和github双平台
    git remote set-url yyy xxx 修改远程仓库连接形式
    git push yyy zzz zzz为分支，看代码仓库中如何定义

    git config user.name / user.email 查看这条电脑git的用户
    git config --global user.name aaa aaa为用户名
    git config --global user.email bbb bbb为邮箱

    初试化仓库后命令行步骤如下：
    git init
    git remote add yyy xxx
    git add .
    git commit -m "自定义内容"
    git push yyy zzz
