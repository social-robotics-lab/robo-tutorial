# 開発環境の構築
全ての手順はインターネットに接続した状態で実施すること。

## Windowsの場合

### Wingetのインストール（Windows10の人のみ。Windows11の人は不要）
- Microsoft Storeのアプリインストーラーにアクセス
- `インストール`ボタンを押し、画面の指示に従ってインストール

### Visual Studio Code（プログラムを書くエディタ）のインストール
- コマンドプロンプトを開く
- コマンドプロンプトに次のコマンドを入力：`winget install Microsoft.VisualStudioCode`

### Pythonのインストール
- コマンドプロンプトに次のコマンドを入力：`winget install python.python.3.12`

### FFmpeg（動画や音声を扱うためのソフトウェア）のインストール
- コマンドプロンプトに次のコマンドを入力：`winget install Gyan.FFmpeg`


### Pythonモジュールのインストール
- コマンドプロンプトを開く
- コマンドプロンプトに次のコマンドを入力：`pip install pydub gtts pysimplegui opencv-python opencv-contrib-python ffmpeg-python`

### Microsoft Azure Python Speech SDK
- Visual C++ 再頒布可能パッケージをインストール
- [公式サイト](https://docs.microsoft.com/ja-JP/cpp/windows/latest-supported-vc-redist?view=msvc-170&preserve-view=true)から「Visual Studio 2015、2017、2019、および 2022」の「X64」をダウンロード＆インストール
- PCを再起動
- コマンドプロンプトを開く
- コマンドプロンプトに次のコマンドを入力：`pip install azure-cognitiveservices-speech`

### プログラム保存場所
- `C:\Users\ユーザ名`の下に`workspace`というフォルダを作成
- このチュートリアルで作成するプログラムは`C:\Users\ユーザ名\workspace`に保存していく


## Macの場合
- Mac App Store から Xcode をインストール（Xcodeはインストールに20～30分かかる。ひたすら待つ）
- terminal.app を起動し、その上で `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"` を実行して homebrew をインストール
- 同じく terminal 上で `brew install python@3.12` で python3.12 がインストールされる
- 同じく terminal 上で `brew install ffmpeg` で ffmpeg をインストール
- あとは python の各モジュールをインストール（`pip3 install`とすること）
