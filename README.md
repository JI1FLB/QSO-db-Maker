　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　2020年1月22日
　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　
　　　　　　　N1MM-Logger-ADIF-to-JARL-contest-logツールについて
　　　　　　　
　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　JI1FLB/田中　盛一
　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　
1.はじめに
本ツールはN1MM Logger+でコンテストに参加した後に、国内コンテストではJARLコンテストログVer2でログ提出する必要があり、また、QSL印刷ではコンテストQSOデータをTurbo Ham Logへデータを入力させて利用する必要があることから、これらの課題を解決するために利用するためのツールである。
なお、本資料は、このツールの使い方を説明するものである。


2.目的
N1MM Logger+でコンテスト参加した後に、JARLコンテストログVer2とTurbo Ham Log用CSVファイルを簡単に生成するため。


3.ソフトウェア概要
3.1　概要
本ツールは、pythonで作ったもので、N1MM Logger+が生成するADIFファイルからJARLコンテストログVer2とTurbo Ham Log用のCSVファイルに変換する。
本ツールは、親父の手習いでこのリバイズからGUI化した。


3.2　ソフトウェアとrevについて
rev1:　ADIFファイル、form.txtをプログラム群と同一フォルダに置き、プログラムを実行するもの
rev2:　ADIFファイル,form.txtのフォルダを選択してプログラムを実行するもの
rev3:　rev1に加えて、過去のQSO状況でQSLを発行するか否かを判断可能なもの
rev4:　ADIFファイル,form.txt,QSO_DB_lib.txtのフォルダを選択してログファイルを生成するもので、過去のQSO状況でQSLを発行するか否かを判断可能なもの


3.3　ソフトウェア構成
メインプログラム：N1MM2JARL-log.py
サブルーチン群：
form_viewer.py：ログサマリーの必要データ記述するform.txtファイルを編集するためのルーチン
Phase0.py：サブルーチン
Phase0_1.py：サブルーチン
Phase1.py：サブルーチン
Phase2.py：サブルーチン
Phase3.py：サブルーチン
QSO_db_maker_rev1.py：Turbo Ham LogでADIFファイルを出力し、そのデータを基のQSデータライブラリを作成するツール。QSOデータライブラリは過去のQSO状況からQSLを発行するか否かを判断するために用いるデータで、「コールサイン」＋「バンド」＋「モード」から構成される。


4.準備
4.0　pythonのインストール：python 3.7,python 3.8
4.1　form.txtの準備
form.txtにコンテストサマリー部分の内容を記入する。
【注意】form.txtのコールサイン（半角）とadifファイルのcallsign.adiのcallsignが同一であること。
4.2　QSOデータライブラリの作成
・Turbo Ham LogでADIFファイルを出力
・QSO_db_maker_rev1.pyを起動し、Turbo Ham logのADIFファイルを指定し、処理を実行する。このツールは、【QSO_DB_lib.txt】を生成する。

5.ソフトウェアの起動
5.1　ソフトウェア起動
N1MM2JARL-log.pyをダブルクリックして、ツールを起動する。または、pythonのIDEからツールを起動する。

5.2　パラメータ設定

5.3　コンテストログ生成
コンテストログ生成ボタンを押して、ログを生成する。
ファイルは複数生成され、コンテストログ、Turbo Ham log用CSVファイル、スコアシートなどを出力する。


6.今後の予定
★pythonのADIF-ioモジュールの活用
2020年1月にpythonのADIF-ioモジュールが存在することが判り、ソフトウェアがコンパクトなるため、このモジュールを利用して開発を行う。

★QSL発行判断の機能追加
無駄なQSL発行を行わないため、JARLの会員情報で判断する。
JARLの会員情報をスクラップするモジュールを既に作成済みであり、早々にこのモジュールを組み込む。


7.ライセンス
MITライセンス