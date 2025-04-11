# RobotControllerとの通信プロトコル

RobotControllerとの通信は、
1. 指令コマンド（play_pose, play_motion, play_wav, etc）の文字列を送信
1. 指令コマンドの引数のデータ（各軸の角度値、各LEDの値、音声等）を送信
というプロトコルで行われます。

それぞれの送信では、
1. 送信データのバイト数を4byte (int) で送信
1. 送信データそのものを送信
しています。

このプロトコルの実装例は、robottools.pyを参照してください。

## play_pose(pose:dict)

### 動作
辞書形式で記述されたポーズ（各軸の角度の指令値）のデータを送信します。RobotControllerではその指令値の通りに軸を動かします。動作コマンドはデフォルトでは22222ポートに送信します。

形式：

    {"Msec": duration, "ServoMap": {"LABEL": value, ...}}

例：

    {"Msec": 1000, "ServoMap": {"BODY_Y": 10, "R_SHOU": 0}}

- Msecは軸の角度が指令値に到達するまでにかかる秒数です。単位はミリ秒で、整数値（int）の値をとります。
- ServoMapは軸のラベル(LABEL)と角度の指令値(value)の対応です。
- 軸のラベルはCommUとSotaで異なります。詳細は[【補足】ロボットの軸情報]を見てください。
- valueの単位は度で、整数値（int）の値をとります。
 

### LED
辞書形式で記述されたLEDのデータを送信します。RobotControllerではその指令値の通りにLEDの明るさを変更します。デフォルトでは22222ポートに送信します。

形式：

    {"Msec": duration, "LedMap": {"LABEL": value, ...}}

例：

    {"Msec": 1000, "LedMap": {L_EYE_R=255, L_EYE_G=0, L_EYE_B=0}}

- MsecはLEDが変化するまでにかかる秒数です。単位はミリ秒で、整数値（int）の値をとります。
- LedMapはLedのラベル(LABEL)と明るさの指令値(value)の対応です。
- LedのラベルはCommUとSotaで異なります。詳細は[【補足】ロボットの軸情報]を見てください。
- valueの0 ~ 255で、整数値（int）の値をとります。


## play_wav(wav_file:str)

wav_fileで指定したパスのWavファイルをバイナリファイルとして読み込み、そのデータを送信します。RobotControllerでは、そのWavファイルの内容を再生します。Wavデータはデフォルトでは22222ポートに送信します（RobotController側の設定ファイルを変更することによって番号を変えられます）。
