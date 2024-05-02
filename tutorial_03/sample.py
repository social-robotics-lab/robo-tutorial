from robottools import RobotTools
import openai
import azure.cognitiveservices.speech as speechsdk
import time

print("準備中")
rt = RobotTools("192.168.11.41", 22222)

# OpenAIのAPIのセットアップ
openai.api_key = "APIキーを入力"
model_engine = "gpt-4-turbo"

# MS Azureの音声認識器を作成
speech_key, service_region = "APIキーを入力", "japanwest"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
speech_config.speech_recognition_language="ja-JP"
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

prompt = [
    {'role': 'system', 'content': 'あなたはユーザーの雑談相手です。'},
    {'role': 'system', 'content': '返事は短めに二文までにしてください。'}
]
print("準備完了。発話を始めてください。")
while True:
    # 音声認識開始
    result = speech_recognizer.recognize_once()

    # 音声認識結果（ユーザの発話）の処理
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("USER:", result.text)
        # プロンプトにユーザの発話を追加
        prompt.append({'role': 'user', 'content': result.text})
        # ユーザの発話をChatGPTに送信、生成された応答文を取得
        response = openai.chat.completions.create(
            model=model_engine,
            messages=prompt
        )
        message = response.choices[0].message.content
        # ロボットに返答を発話させる
        # d = rt.say_text(message)
        # m = rt.make_beat_motion(d, speed=1.5)
        # rt.play_motion(m)
        # プロンプトにロボット（Assistant）の発話を追加
        prompt.append({"role": "assistant", "content": message})
        print("ROBOT:", message)
        # 発話中は音声認識を止める
        # time.sleep(d)
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(result.no_match_details))
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))

    if result.text.startswith('終了'):
        break
