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
        img = img.convert("YCbCr")
        img = ImageOps.fit(img, (HEIGHT, WIDTH), Image.ANTIALIAS)
        img_data = np.asarray(img, dtype=np.float32)
        img_data = img_data / 127.0 - 1
        imgs_data.append(img_data)
    return imgs_data


def create_labels(each_class_num):
    labels = []
    current = 0
    for boundary in each_class_num:
        for i in range(boundary):
            labels.append(current)
        current += 1
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
    each_class_num = []
    all_files = []
    class_count = request.form.get('count')
    for i in range(int(class_count)):
        index = i + 1
        one_class_files = request.files.getlist('label' + str(index) + '_imgs')
        for file in one_class_files:
            all_files.append(file)
        each_class_num.append(len(one_class_files))
    input_data = process_img(all_files)
    label = create_labels(each_class_num)
    epoch, batch_size, learning_rate, user_id = get_parameters(request.form)
    imageClassifier.training(np.array(input_data), np.array(label), int(epoch), int(batch_size), float(learning_rate), user_id, class_count)
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
    result = []
    for one in prediction[0]:
        result.append(round(float(one)))
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
    class_num = int(request.form.get('count'))
    labels = []
    for i in range(class_num):
        actual_index = str(i + 1)
        labels.append(request.form.get('label' + actual_index))
    path = user_id + '/labels.txt'
    with open(path, 'w+') as file:
        # 清空文件内容
        file.seek(0)
        file.truncate()
        for label in labels:
            file.write(label + '\n')
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
