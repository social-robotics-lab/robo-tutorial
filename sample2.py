from robottools import RobotTools
import PySimpleGUI as sg

rt = RobotTools('192.168.11.41', 22222)

# GUI設定
sg.theme()
# ウインドウのレイアウトの作成
# レイアウトはグリッド（2次元リスト）で表現される
layout = []

# モーションボタンのレイアウト
layout.append(
    [
        sg.Button('アイドルモーション開始', key='idle'),
        sg.Button('アイドルモーション停止', key='stop'),
        sg.Button('ポーズリセット', key='reset')    
    ]
)

# 発話ボタンのレイアウト
text_1 = 'こんにちは。ぼくはソータです。'
layout.append(
    [
        sg.Text(text_1, size=(50, 1)),
        sg.Button('発話', key='speak_1')
    ]
)

text_2 = '同志社大学文化情報学部へようこそ。'
layout.append(
    [
        sg.Text(text_2, size=(50, 1)),
        sg.Button('発話', key='speak_2')
    ]
)

text_3 = 'これからどうぞ、よろしくお願いします。'
layout.append(
    [
        sg.Text(text_3, size=(50, 1)),
        sg.Button('発話', key='speak_3')
    ]
)

# テキストの自由入力
layout.append(
    [
        sg.InputText(key='free_speech_field', size=(50, 1)),
        sg.Button('発話', key='speak_free')
    ]
)


# ウインドウにレイアウトを設定
window = sg.Window('Sota controller', layout)

# Event loop
while True:
    event, values = window.read(timeout=1)
    if event is None:
        print('Window event is None. exit')
        break
    elif event == 'speak_1':
        d = rt.say_text(text_1)
        m = rt.make_beat_motion(d)
        rt.play_motion(m)
    elif event == 'speak_2':
        d = rt.say_text(text_2)
        m = rt.make_beat_motion(d)
        rt.play_motion(m)
    elif event == 'speak_3':
        d = rt.say_text(text_3)
        m = rt.make_beat_motion(d)
        rt.play_motion(m)
    elif event == 'speak_free':
        d = rt.say_text(values['free_speech_field'])
        m = rt.make_beat_motion(d)
        rt.play_motion(m)
    elif event == 'idle':
        rt.play_idle_motion()
    elif event == 'stop':
        rt.stop_idle_motion()
    elif event == 'reset':
        servo_map = dict(HEAD_R=0, HEAD_P=-5, HEAD_Y=0, BODY_Y=0, 
                         L_SHOU=-90, L_ELBO=0, R_SHOU=90, R_ELBO=0)
        pose = dict(Msec=500, ServoMap=servo_map)
        rt.play_pose(pose)
    else:
        pass

window.close()