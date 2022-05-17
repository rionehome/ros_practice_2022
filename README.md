# ros_practice_2022

**パソコンからgithubへの更新**
  -$git add (ファイル名)
  -$git commit -m "(メッセージ)
  -$git push origin (ブランチ名)

  <dt>ブランチの作成
    <dd>git branch (ブランチ名)</dd>
 
  <dt>ブランチの切り替え</dt>
    <dd>git checkout (ブランチ名)</dd>

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

<dl>
  <dt>その他</dt>
    <dd>rosnode list</dd>
    <dd>rosnode info (ノード名)</dd>
    <dd>rostopic list</dd>
    <dd>rostopic info (トピック名)</dd>
    <dd>rostopic echo (トピック名)</dd>
    <dd>rosrun rqt_graph rqt_graph</dd>
    <dd>roslaunch (パッケージ名) (ローンチファイル名)</dd>
</dl>


