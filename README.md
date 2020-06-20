# Teachable Machine

 At present,  we implemented the  Google Teachable Machine‘s image classification.



### Start front end

```shell
cd "Teachable Machine/app"
npm install
npm run dev
```



### Start back end

```shell
cd "Teachable Machine/backend"
pip install -r requirements.txt
py app.py
```



Then, you can visit  http://localhost:8080/ImageClassifier  to train model and export model.



Then you can  apply the model to an Android application. For project **tflite_demo**, you can put **my_model.tflite** and **labels.txt** in **/app/src/main/assets**.

