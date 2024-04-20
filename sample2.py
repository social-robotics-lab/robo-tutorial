import tkinter as tk
from robottools import RobotTools

rt = RobotTools(ip="192.168.11.41", port=22222)

def start_idle():
    # アイドルモーションを開始する
    rt.play_idle_motion()

def stop_idle():
    # アイドルモーションを終了する
    rt.stop_idle_motion()
    
def reset_pose():
    # ポーズをリセットする
    servo_map = dict(HEAD_R=0, HEAD_P=-5, HEAD_Y=0, BODY_Y=0, 
                     L_SHOU=-90, L_ELBO=0, R_SHOU=90, R_ELBO=0)
    pose = dict(Msec=1000, ServoMap=servo_map)
    rt.play_pose(pose)

def say_text(text:str):
    # 引数で与えた文字列を発話
    rt.say_text(text)

# メインウィンドウを作成
root = tk.Tk()
root.title("RobotContrller GUI")

# 1段目のフレーム（ボタンを3つ置く）
frame1 = tk.Frame(root)
frame1.pack(fill='x', padx=10, pady=5)

# 1段目
button1_1 = tk.Button(frame1, text="アイドルモーション開始", command=start_idle)
button1_1.pack(side="left", padx=10)
button1_2 = tk.Button(frame1, text="アイドルモーション停止", command=stop_idle)
button1_2.pack(side="left", padx=10)
button1_3 = tk.Button(frame1, text="ポーズリセット", command=reset_pose)
button1_3.pack(side="left", padx=10)

# 2段目のフレーム（ラベルとボタン用）
frame2 = tk.Frame(root)
frame2.pack(fill='x', padx=10, pady=5)

# 2段目
label2_1_text = tk.StringVar()
label2_1_text.set("こんにちは。ぼくはソータです。")
label2_1 = tk.Label(frame2, textvariable=label2_1_text)
label2_1.pack(side="left", padx=10)
button2_2 = tk.Button(frame2, text="発話", command=lambda: say_text(label2_1_text.get()))
button2_2.pack(side="right", padx=10)

# 3段目のフレーム（ラベルとボタン用）
frame3 = tk.Frame(root)
frame3.pack(fill='x', padx=10, pady=5)

# 3段目
label3_1_text = tk.StringVar()
label3_1_text.set("同志社大学文化情報学部へようこそ。")
label3_1 = tk.Label(frame3, textvariable=label3_1_text)
label3_1.pack(side="left", padx=10)
button3_2 = tk.Button(frame3, text="発話", command=lambda: say_text(label3_1_text.get()))
button3_2.pack(side="right", padx=10)

# 4段目のフレーム（ラベルとボタン用）
frame4 = tk.Frame(root)
frame4.pack(fill='x', padx=10, pady=5)

# 4段目
label4_1_text = tk.StringVar()
label4_1_text.set("これからどうぞ、よろしくお願いします。")
label4_1 = tk.Label(frame4, textvariable=label4_1_text)
label4_1.pack(side="left", padx=10)
button4_2 = tk.Button(frame4, text="発話", command=lambda: say_text(label4_1_text.get()))
button4_2.pack(side="right", padx=10)

# 5段目のフレーム（エントリーフィールドとボタン用）
frame5 = tk.Frame(root)
frame5.pack(fill='x', padx=10, pady=5)

# 5段目
entry = tk.Entry(frame5)
entry.pack(side="left", padx=10, expand=True, fill='x')  # expandとfillを使用してエントリーを広げる
button5_1 = tk.Button(frame5, text="発話", command=lambda: say_text(entry.get()))
button5_1.pack(side="right", padx=10)

# イベントループに入る
root.mainloop()
