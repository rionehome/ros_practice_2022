# ros_practice_2022
  
  


**パソコンからgithubへの更新**
  - git add (ファイル名)  
  - git commit -m "(メッセージ)"  
  - git push origin (ブランチ名)  

**ブランチの作成**
  - git branch (ブランチ名)  
 
**ブランチの切り替え**
  - git checkout (ブランチ名)  

**githubからパソコンへの更新**
  - git pull origin (ブランチ名)  
  
**パッケージの情報をrosシステムへ更新**
  - cd (ワークスペース)  
  - catkin_make  
  (ターミナルを開いたままの場合)  
  コマンドへの更新  
  - source devel/setup.bash  
  
**ros実行**
  - roscore  
  - rosrun (パッケージ名) (ファイル名)  
  
  
**その他**
  - rosnode list  
  - rosnode info (ノード名)  
  - rostopic list  
  - rostopic info (トピック名)  
  - rostopic echo (トピック名)  
  - rosrun rqt_graph rqt_graph  
  - roslaunch (パッケージ名) (ローンチファイル名)  
