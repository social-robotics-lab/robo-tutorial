# Sotaのネットワークへの接続
- Sotaを学校や自宅のネットワークに接続するには、[QRコードで接続](https://vstone.co.jp/sotamanual/index.php?QR%E3%82%B3%E3%83%BC%E3%83%89%E3%81%A7%E6%8E%A5%E7%B6%9A)を利用する。

# SotaのIPアドレスの確認
- ネットワークに接続できたら、[IPアドレスの確認](https://vstone.co.jp/sotamanual/index.php?%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E7%B5%8C%E7%94%B1%E3%81%A7%E3%83%AD%E3%82%B0%E3%82%A4%E3%83%B3%E3%81%99%E3%82%8B#f061e62f)を行う。
- SotaがIPアドレスを発話するので、メモしておく。

# Sotaにログイン
- PC上でコマンドプロンプトを開く
- `ssh root@192.168.11.10`を入力。ただし、「192.168.11.10」の部分は実際のSotaのIPアドレスを入力。
- passwordは`edison00`。passwordで入力した文字は見えないが入力自体はされている。
- 新しいIPアドレスが変更されていた場合、以下のような表示が出ることがある。
```
The authenticity of host '...' can't be established.
RSA key fingerprint is SHA256:....
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```
- これはSSHサーバが本当に接続したいSSHサーバかどうかを確認するメッセージである。これが表示された場合、`yes`と入力。

# RobotControllerの起動と終了
- Sotaにログインしている状態で、以下を実行。
- `cd ~/RobotController_bin`を入力。
- `java -jar RobotController.jar`を入力。
- 実行後、サーボモーターに電流が入り軸が固定される。この状態になると、外部のクライアントプログラムからのコマンドを受けつけられる。
- RobotControllerを終了する時は`ctrl + c`を入力。
- SSHを終了するには、`exit`を入力。
