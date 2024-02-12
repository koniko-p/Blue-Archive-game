关于ba的混枪游戏。

dev分支
1. git clone 来将项目放入本地仓库
2.使用git checkout -b dev origin/dev获取dev分支的内容
3.git remote add upstream git@github.com:koniko-p/Blue-Archive-game.git 来保持同步
4.最后将最新版分合并到自己本地仓库

Reminder：
1.一切修改先用dev分支。
2.最后再git上先换到master，再用git merge dev合并，最后push到github上即可。

资源：
1. https://www.zhihu.com/question/385197253 （c++ game）