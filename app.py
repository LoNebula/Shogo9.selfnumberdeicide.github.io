from flask import Flask, render_template, request, send_file
import random
import os
import pathlib


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'test' not in request.files:
        return 'No file part'
    file = request.files['test']
    if file.filename == '':
        return 'No selected file'

    # ファイル名とファイル名の拡張子を分離する
    filename, ext = os.path.splitext(file.filename)

    # HTMLから受け取った数値でファイル名の長さを決める
    filename_length = int(request.form.get('filename_length', 10))
    new_filename = generate_random_filename(filename_length) + ext

    save_directory = request.form.get('save_directory', '/default/save/directory')

    # ファイルを保存する
    file_path = os.path.join(save_directory, new_filename)
    file.save(file_path)

    # ファイルをダウンロードさせる
    return send_file(file_path, as_attachment=True, download_name=new_filename)

def generate_random_filename(length):
    text = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    filename = ''.join(random.choices(text, k=length))
    return filename

if __name__ == "__main__":
    app.run()