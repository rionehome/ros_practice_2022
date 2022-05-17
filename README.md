# ros_practice_2022
  

**よく使うLinuxコマンド**
  - sudo    
  - sudo su  
  - apt  
  - pwd  
  - cd  
  - ls   
  - ls -a  
  - ls -l   
  - mv  
  - echo  
  - cat  
  - vim  
  - chmod (+,-,=)(権限) (ファイル名)  
  ('-'or'd')(admin)(local)(others)
    | do  | num |
    |:---:|:---:|
    |r    |4    |
    |w    |2    |
    |x    |1    |

**ワークスペースの作成**
  - mkdir -p (ワークスペース名)/src
  - cd (ワークスペース名)/src
  - catkin_init_workspace
  - cd ..
  - catkin_make
  - echo "source (ワークスペースまでのパス)/devel/setup.bash" >> ~/.bashrc

**パッケージの作成**
  - cd (ワークスペースまでのパス)/src
  - catkin_create_pkg (パッケージ名)
  - cd ..
  - catkin_make

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
  - rosmsg show (メッセージ名)
  - rosnode list  
  - rosnode info (ノード名)  
  - rostopic list  
  - rostopic info (トピック名)  
  - rostopic echo (トピック名)  
  - rosrun rqt_graph rqt_graph  
  - roslaunch (パッケージ名) (ローンチファイル名)  
