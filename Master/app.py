from flask import Flask, render_template, request, redirect, url_for

import json

app = Flask(__name__)

# 勝負判定用リスト
hantei = [0] * 9

# マルバツ画像URL入りJSON（予定）
def get_profile():
    file_json = "data/marubatu.json"
    prof = open(file_json,encoding='utf-8')
    json_str = prof.read()
    prof.close()
    prof_dict = json.loads(json_str)
    return prof_dict

# ファイル書き換え
def change_list(num):
    f = open('data/marubatu.json', 'w')
    json.dump(num, f)
    f.close()

# POPUP利用
@app.route('/marubatu_popup')
def marubatu_popup():
    prof_dict = get_profile()
    return render_template('marubatu_popup.html', title='marubatu game', user=prof_dict, hantei=hantei)

# マルを押した時
@app.route('/change_maru')
def change_maru():
    num = int(request.args.get('num'))
    prof_dict = get_profile()
    prof_dict[num] = 'maru.jpeg'
    hantei[num] = 1
    change_list(prof_dict)
    return redirect(url_for("marubatu_popup"))

# バツを押した時
@app.route('/change_batu')
def change_batu():
    num = int(request.args.get('num'))
    prof_dict = get_profile()
    prof_dict[num] = 'batu.jpeg'
    hantei[num] = 4
    change_list(prof_dict)
    return redirect(url_for("marubatu_popup"))

# リセットボタン
@app.route('/reset')
def reset():
    global hantei
    hantei = [0] * 9
    prof_dict = get_profile()
    prof_dict = ["siro.jpeg", "siro.jpeg", "siro.jpeg", "siro.jpeg", "siro.jpeg", "siro.jpeg", "siro.jpeg", "siro.jpeg", "siro.jpeg"]
    change_list(prof_dict)
    return redirect(url_for("marubatu_popup"))
    
if __name__ == "__main__":
    app.run(debug=True)