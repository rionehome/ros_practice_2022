# ros_practice_2022

<dl>
  <dt>パソコンからgithubへの更新</dt>
    <dd>git add (ファイル名)</dd>
    <dd>git commit -m "(メッセージ)</dd>
    <dd>git push origin (ブランチ名)</dd>

  <dt>ブランチの作成
    <dd>git branch (ブランチ名)</dd>
 
  <dt>ブランチの切り替え</dt>
    <dd>git checkout (ブランチ名)</dd?

  <dt>githubからパソコンへの更新</dt>
    <dd>git pull origin (ブランチ名)</dd>
  
  <dt>パッケージの情報をrosシステムへ更新</dt>
    <dd>cd (ワークスペース)</dd>
    <dd>catkin_make</dd>
    
    <dd>(ターミナルを開いたままの場合)</dd>
    <dd>コマンドへの更新</dd>
    <dd>source devel/setup.bash</dd>
  
  <dt>ros実行</dt>
    <dd>roscore</dd>
    <dd>rosrun (パッケージ名) (ファイル名)</dd>

</dl>
  


その他

  rosnode list
  
  rosnode info (ノード名)
  
  rostopic list
  
  rostopic info (トピック名)
  
  rostopic echo (トピック名)
  

  rosrun rqt_graph rqt_graph


  roslaunch (パッケージ名) (ローンチファイル名)


