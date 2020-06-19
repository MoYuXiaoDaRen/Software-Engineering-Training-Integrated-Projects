import os
import shutil

from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import imageClassifier
from PIL import Image, ImageOps
import io
import numpy as np

app = Flask(__name__)
CORS(app, supports_credentials=True)

HEIGHT = 224
WIDTH = 224


def process_img(files):
    imgs_data = []
    for i in range(len(files)):
        f = files[i]
        file_storage = f.read()
        byte_stream = io.BytesIO(file_storage)
        img = Image.open(byte_stream)
        img = ImageOps.fit(img, (HEIGHT, WIDTH), Image.ANTIALIAS)
        img_data = np.asarray(img, dtype=np.float32)
        img_data = img_data / 127.0 - 1
        imgs_data.append(img_data)
    return imgs_data


def create_labels(total, boundary):
    labels = []
    for i in range(total):
        if i < boundary:
            labels.append(0)
        else:
            labels.append(1)
    return labels


def get_parameters(form):
    epoch = form.get('epoch')
    batch_size = form.get('batch')
    learning_rate = form.get('learning_rate')
    user_id = request.form.get('userID')
    return epoch, batch_size, learning_rate, user_id


@app.route('/CheckID', methods=['POST'])
def check_id():
    user_id = request.form.get('userID')
    if not os.path.exists(user_id):
        os.makedirs(user_id)
        return jsonify('TRUE')
    else:
        return jsonify('FALSE')


@app.route('/imagesTraining', methods=['POST'])
def get_img():
    class2_files = request.files.getlist('label2_imgs')
    all_files = request.files.getlist('label1_imgs')
    for i in range(len(class2_files)):
        all_files.append(class2_files[i])
    input_data = process_img(all_files)
    label = create_labels(len(all_files), len(request.files.getlist('label1_imgs')))
    epoch, batch_size, learning_rate, user_id = get_parameters(request.form)
    imageClassifier.training(np.array(input_data), np.array(label), int(epoch), int(batch_size), float(learning_rate), user_id)

    return jsonify('上传成功')


@app.route('/imagesPrediction', methods=['POST'])
def predict_img():
    f = request.files['predict_img']
    file_storage = f.read()
    byte_stream = io.BytesIO(file_storage)
    img = Image.open(byte_stream)
    img = ImageOps.fit(img, (HEIGHT, WIDTH), Image.ANTIALIAS)
    user_id = request.form.get('userID')
    img_data = np.asarray(img, dtype=np.float32)
    img_data = img_data / 127.0 - 1
    h, w, c = img_data.shape
    img_data = img_data.reshape((1, h, w, c))
    prediction = imageClassifier.prediction(img_data, user_id)
    result = [round(float(prediction[0][0])), round(float(prediction[0][1]))]
    return jsonify(result)


@app.route('/modelExport', methods=['POST'])
def export_model():
    user_id = request.form.get('userID')
    model_type = request.form.get('model_type')
    if model_type == 'h5':
        path = user_id + '/my_model.h5'
    elif model_type == 'tflite':
        imageClassifier.h5_to_tflite(user_id)
        path = user_id + '/my_model.tflite'
    try:
        return send_from_directory(app.root_path, path, as_attachment=True)
    except Exception as e:
        return jsonify({"code": "异常", "message": "{}".format(e)})


@app.route('/labelExport', methods=['POST'])
def export_label():
    user_id = request.form.get('userID')
    label1 = request.form.get('label1')
    label2 = request.form.get('label2')
    path = user_id + '/labels.txt'
    with open(path, 'w+') as file:
        # 清空文件内容
        file.seek(0)
        file.truncate()
        file.write(label1 + '\n')
        file.write(label2 + '\n')
        file.close()
    try:
        return send_from_directory(app.root_path, path, as_attachment=True)
    except Exception as e:
        return jsonify({"code": "异常", "message": "{}".format(e)})




@app.route('/leave', methods=['POST'])
def clear_model():
    user_id = request.form.get('userID')
    print('清理文件夹')
    if os.path.exists(user_id):
        shutil.rmtree(user_id)
    return jsonify('Successfully')


@app.route('/soundsClassifier', methods=['POST'])
def get_sound():
    f1 = request.files['sound_1']
    f1.save(f1.filename)
    print(request.files)
    print(request.form)
    """
    tensorflow
    """
    return jsonify('上传成功')


@app.route('/posesClassifier', methods=['POST'])
def get_pose():
    print(request.files)
    print(request.form)
    """
    tensorflow
    """
    return jsonify('上传成功')


if __name__ == '__main__':
    # 前后端处于局域网
    # app.run(host='0.0.0.0', threaded=True, debug=True)
    # 前后端同一台机器
    app.run(threaded=True, debug=True)
