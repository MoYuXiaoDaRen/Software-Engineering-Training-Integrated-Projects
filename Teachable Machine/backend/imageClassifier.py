import tensorflow as tf
from tensorflow.keras import layers, models, optimizers, backend
import numpy as np
import os

# 不使用GPU
# os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

'''
def create_model(h, w, c):
    model = models.Sequential()
    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(h, w, c)))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.Flatten())
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(2))
    return model
'''


def create_model(h, w, c, class_count):
    model = models.Sequential()
    model.add(layers.Conv2D(6, (5, 5), padding='same', input_shape=(h, w, c)))
    model.add(layers.BatchNormalization())
    model.add(layers.Activation(activation='relu'))
    model.add(layers.MaxPooling2D((2, 2), strides=2, padding='same'))
    # model.add(layers.Dropout(0.2))
    model.add(layers.Flatten())
    model.add(layers.Dense(256, activation='relu'))
    # model.add(layers.Dropout(0.2))
    model.add(layers.Dense(class_count, activation='softmax'))
    return model


def training(input_data, label, epoch, batch_size, learning_rate, user_id, class_count):
    backend.clear_session()
    _, h, w, c = input_data.shape
    model = create_model(h, w, c, class_count)
    optimizer = optimizers.Adam(learning_rate=learning_rate)
    model.compile(optimizer=optimizer,
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])
    model.fit(input_data, label, batch_size=batch_size, epochs=epoch)
    path = user_id + '/my_model.h5'
    model.save(path)


def prediction(input_data, user_id):
    path = user_id + '/my_model.h5'
    model = models.load_model(path)
    print('Load model succeed!')
    # probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
    # predict = probability_model.predict(input_data)
    predict = model.predict(input_data)
    print(predict)
    return predict


def h5_to_tflite(user_id):
    backend.clear_session()
    np.set_printoptions(suppress=True)
    path = user_id + '/my_model.h5'
    output_path = path[:-3] + '.tflite'
    if not os.path.exists(output_path):
        h5_model = models.load_model(path)
        converter = tf.lite.TFLiteConverter.from_keras_model(h5_model)
        converter.post_training_quantize = True
        tflite_model = converter.convert()
        open(output_path, "wb").write(tflite_model)
