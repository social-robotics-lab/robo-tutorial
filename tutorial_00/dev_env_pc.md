# 開発環境の構築
全ての手順はインターネットに接続した状態で実施すること。

## Windowsの場合

### Wingetのインストール（Windows10の人のみ。Windows11の人は不要）
- Microsoft Storeのアプリインストーラーにアクセス
- `インストール`ボタンを押し、画面の指示に従ってインストール

### Visual Studio Code（プログラムを書くエディタ）のインストール
- コマンドプロンプトを開く
- コマンドプロンプトに次のコマンドを入力：`winget install Microsoft.VisualStudioCode`

### FFmpeg（動画や音声を扱うためのソフトウェア）のインストール
- コマンドプロンプトに次のコマンドを入力：`winget install Gyan.FFmpeg`

### Pythonのインストール
- コマンドプロンプトに次のコマンドを入力：`winget install python.python.3.12`

### 再起動
- ここまで終了したら、コマンドプロンプトを閉じ、PCを再起動する

### Pythonモジュール(pydub,gttsなど)のインストール
- コマンドプロンプトを開く
- コマンドプロンプトに次のコマンドを入力：`pip install pydub gtts FreeSimpleGUI opencv-python opencv-contrib-python ffmpeg-python openai`

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
- Mac App StoreからXcodeをインストール（Xcodeはインストールに20～30分かかる。ひたすら待つ）
- terminalというアプリケーションを起動
- terminalに以下の内容を丸ごとコピペし、実行

```zsh
# xcodeのライセンスに同意する(xcodeを入れた後でないとbrewが入らない)
sudo xcodebuild -lisence

# brewのインストール
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# brewのpathを変更する
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"

# 必要なパッケージのインストール
brew install python@3.12
brew install ffmpeg
brew install portaudio

# pipでのパッケージインストール
pip3 install pydub gtts FreeSimpleGUI opencv-python opencv-contrib-python ffmpeg-python openai azure-cognitiveservices-speech pyaudio
```

### プログラム保存場所
- ホームディレクトリ(`/Users/ユーザ名`)の下に`workspace`というフォルダを作成
- このチュートリアルで作成するプログラムは`/Users/ユーザ名/workspace`に保存していく
