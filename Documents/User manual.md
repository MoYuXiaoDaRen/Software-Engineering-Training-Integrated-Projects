# User manual（用户使用手册）

## Developer deployment（开发人员部署）

### Start server（启动后台） 

```shell
cd "Teachable Machine/backend"
pip install -r requirements.txt
py app.py
```

###  Start the front-end（启动前端）

```shell
cd "Teachable Machine/app"
npm install
npm run dev
```

## For ordinary user（普通用户使用）

Please enter http://localhost:8080/ImageClassifier (or public_IP:8080/ImageClassifier) in the browser.

浏览器输入 http://localhost:8080/ImageClassifier （或公网ip:8080/ImageClassifier ）。

![01](md_img\01.png)

### Determine the ID（确定ID）

First, user needs to input an ID number. The server will detect whether this ID already exists. If so, please replace it. 

首先需要用户输入一个ID号，后台会检测此ID是否已经存在，若存在，请更换一个。

If the ID is created successfully, you can see the button of **Upload Image** and the button to switch the camera can be clicked, and the user cannot change the ID again:

若ID创建成功，可以看到**Upload Image**的按钮以及切换摄像头的按钮可以点击，且用户不可再更改ID：

![02](md_img\02.png)

If the ID entered is already occupied by another user, the following alert appears: 

若输入的ID已被其他用户占用，则出现以下提示：

![03](md_img\03.png)

### Upload training data（上传训练数据）

Users have three ways to upload images:

用户有三种方式上传照片：

1. Drag to upload local photos 

   拖拽上传本地照片

   ![04](md_img\04.png)

2. Click the Upload button and select local photo to upload

   点击上传按钮选择本地照片上传

   ![05](md_img\05.png)

3. Use the webcam to get images 

   使用网络摄像头获取照片

   ![06](md_img\06.png)

   Note that the image is automatically cropped in the server and the middle section is selected. 

   注意，图片会在后台自动裁剪，选取中间部分。

   In addition, user can customize the class name:

   此外用户还可以自定义类名：

   ![07](md_img\07.png)

### Training model（训练模型）

Only when the user has filled in the class name and uploaded images can he or she click the **Train Model** button. 

只有当用户两个类都填写了类名和上传了图片，才可以点击**Train Model**按钮。

![08](md_img\08.png)

User can also customize the training parameters.  Moving the mouse to the question icon, you can see the function of corresponding parameter. 

用户还可以自定义训练参数，鼠标移动到问号图标，可以显示对应参数的作用。

![09](md_img\09.png)

Click the **Train Model** button and wait for the completion of server training. 

点击**Train Model**按钮，等待后台训练完成。

![10](md_img\10.png)

### Prediction（预测）

After the training, user can upload a image or choose the webcam to take a picture to predict. 

训练完成后，用户可以上传一张图片或者选择网络摄像头拍照进行预测。

After uploading the image, click the **Predict** button, and wait for the server's prediction to complete and returning the prediction result. 

上传图片后，点击**Predict**按钮，等待后台预测完成，返回预测结果。

![11](md_img\11.png)

### Export  the model（导出模型）

After model training completed, user can click **Export Model** to Export the Model. 

模型训练完毕后，用户可以点击**Export Model**导出模型。

User can choose the type of model to export, and there are corresponding instructions. 

用户可以选择导出的模型类型，并且有对应的使用说明。

![12](md_img\12.png)