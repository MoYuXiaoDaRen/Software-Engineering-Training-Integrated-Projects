<template>
  <div v-title data-title="Image Classifier" id="img_classifier">
    <div id="user-id">
      <div id="input-id">
        <el-input
          id="id-text"
          placeholder="Please enter User ID"
          v-model="user_ID"
          :disabled="check_ID_pass"
          clearable>
        </el-input>
      </div>
      <el-button
        id="check-id-btn"
        type="primary"
        plain
        @click="checkID()"
        :disabled="check_ID_pass">
        Check ID
      </el-button>
    </div>
    <div class="class-box" id="box1">
      <div class="label-box">
        <el-input
          class="label-name"
          id="label1"
          placeholder="Please enter Class1 label"
          prefix-icon="el-icon-edit"
          v-model="label1_value"
          @change="label_change()"
          :disabled="!check_ID_pass"
          clearable>
        </el-input>
      </div>
      <div class="choose-show-box">
        <div class="mode-box">
          <el-switch
            @change="changeMode('class1-change')"
            class="change-mode"
            id="class1-change"
            v-model="is_camera1"
            active-text="Webcam"
            :disabled="!check_ID_pass"
            inactive-text="Upload">
          </el-switch>
          <div class="webcam-box" v-show="is_camera1">
            <span class="mode-text">Webcam</span>
            <video class="webcam-display" id="class1_video"></video>
            <canvas hidden="hidden" class="canvas-display" id="class1_canvas"  width="1280px" height="720px"></canvas>
            <button
              class="b1"
              @click="setImage1()"
              id="drawb1"
              :disabled="!check_ID_pass">
              Photograph
            </button>
          </div>
          <div class="file-box" v-show="!is_camera1">
            <span class="mode-text">Files</span>
            <div class="dropBox" id="dropBox1" :disabled="!check_ID_pass">
              <img src="../assets/文件.png" class="folder_img">
              <div class="drap-content">Drag images file from your files</div>
            </div>
            <div class="upload_btn_div">
              <button
              class="upload_btn"
              @click="change_input($event)"
              id="btn1"
              :disabled="!check_ID_pass">
              Upload Images
              </button>
            </div>
            <div class="pre_img_decript">
              <div class="img_div">
                <img src="../assets/图片2.png" class="file-box-imgs">
                <img src="../assets/箭头.png" class="file-box-imgs">
                <img src="../assets/图片2.png" class="file-box-imgs">
                <div class="crop_size"></div>
              </div>
              <div class="crop_decript">Images will be cropped to square</div>
            </div>
          </div>
        </div>
        <div class="show-box">
          <div class="show-description">
            Add Images Samples:
          </div>
          <form id="class1_form">
            <div class="img-wrapper" id="img-wrapper1" @click="deleteImg($event)"></div>
          </form>
        </div>
      </div>
    </div>
    <div class="class-box" id="box2">
      <div class="label-box">
        <el-input
          class="label-name"
          id="label2"
          placeholder="Please enter Class2 label"
          prefix-icon="el-icon-edit"
          @change="label_change()"
          v-model="label2_value"
          :disabled="!check_ID_pass"
          clearable>
        </el-input>
      </div>
      <div class="choose-show-box">
        <div class="mode-box">
          <el-switch
            class="change-mode"
            @change="changeMode('class2-change')"
            id="class2-change"
            v-model="is_camera2"
            active-text="Webcam"
            :disabled="!check_ID_pass"
            inactive-text="Upload">
          </el-switch>
          <div class="webcam-box" v-show="is_camera2">
            <span class="mode-text">Webcam</span>
            <video class="webcam-display" id="class2_video"></video>
            <canvas hidden="hidden" class="canvas-display" id="class2_canvas"    width="1280px" height="720px"></canvas>
            <button class="b1" @click="setImage2()" id="drawb2">Photograph</button>
          </div>
          <div class="file-box" v-show="!is_camera2">
            <span class="mode-text">Files</span>
            <div class="dropBox" id="dropBox2" :disabled="!check_ID_pass">
              <img src="../assets/文件.png" class="folder_img">
              <div class="drap-content">Drag images file from your files</div>
            </div>
            <div class="upload_btn_div">
              <button
              class="upload_btn"
              @click="change_input($event)"
              id="btn2"
              :disabled="!check_ID_pass">
              Upload Image
              </button>
            </div>
            <div class="pre_img_decript">
              <div class="img_div">
                <img src="../assets/图片2.png" class="file-box-imgs">
                <img src="../assets/箭头.png" class="file-box-imgs">
                <img src="../assets/图片2.png" class="file-box-imgs">
                <div class="crop_size"></div>
              </div>
              <div class="crop_decript">Images will be cropped to square</div>
            </div>
          </div>
        </div>
        <div class="show-box">
          <div class="show-description">
            Add Images Samples:
          </div>
          <form id="class2_form">
            <div class="img-wrapper" id="img-wrapper2" @click="deleteImg($event)"></div>
          </form>
        </div>
      </div>
    </div>
    <form id="addTextForm" @change="setImg($event)">
      <input type='file' class="upload_file" multiple id="upload_file1" accept = 'image/jpeg,image/jpg,image/png,image/bmp'/>
      <input type='file' class="upload_file" multiple id="upload_file2" accept = 'image/jpeg,image/jpg,image/png,image/bmp'/>
    </form>
    <!-- Training模块样式 -->
    <div id="setting">
      <!-- Train Model按钮 -->
      <div id="train_btn_div">
        <div id="train_text">Training</div>
        <button id="train_model_btn" type="button" @click="submit()" :disabled="train_disable" v-loading.fullscreen.lock="waiting_display">Train Model</button>
        <div id="waiting_content">Please wait......</div>
      </div>
      <!-- Epoch输入 -->
      <div id="epoch_div">
        <div id="advance">Advanced</div>
        <br>
        <form id="epoch_form">
          <span style="font-weight: bold">Epochs: </span>
          <input
            type="number"
            class="train_info"
            id="epochs"
            value="50"
            onkeyup="value=value.replace(/^(0+)|[^\d]+/g,'')"
            :disabled="train_disable"/>
        </form>
        <div class="more_info">
          <img class="question" id="epo_ques" src="../assets/问号.png">
          <div id="epo_detail">
            <div class="detail_title">
              Epochs
            </div>
            <div class="detail_content">
              One epoch means that each and every sample in the training dataset has been fed through the training model at least once. If your epochs are set to 50, for example, it means that the model you are training will work through the entire training dataset 50 times. Generally the larger the number, the better your model will learn to predict the data.
              <br>
              <br>
              You probably want to tweak (usually increase) this number until you get good predictive results with your model.
            </div>
          </div>
        </div>
      </div>
      <!-- Batch size选择 -->
      <div id="batch_div">
        <form id="batch_form">
          <span style="font-weight: bold">Batch Size: </span>
          <select class="train_info" id="batch" :disabled="train_disable">
            <option value ="16">16</option>
            <option value ="32">32</option>
            <option value="64">64</option>
            <option value="128">128</option>
            <option value="256">256</option>
            <option value="512">512</option>
          </select>
        </form>
        <div class="more_info">
          <img class="question" id="bat_ques" src="../assets/问号.png">
          <div id="bat_detail">
            <div class="detail_title">
              Batch Size
            </div>
            <div class="detail_content">
              A batch is a set of samples used in one iteration of training. For example, let's say that you have 80 images and you choose a batch size of 16. This means the data will be split into 80 / 16 = 4 batches. Once all 4 batches have been fed through the model, exactly one epoch will be complete.
              <br>
              <br>
              You probably won't need to tweak this number to get good training results.
            </div>
          </div>
        </div>
      </div>
      <!-- Learning rate输入 -->
      <div id="lr_div">
        <form id="lr_form">
          <div style="font-weight: bold">Learning rate: </div>
          <input
            type="number"
            class="train_info"
            id="learning_rate"
            value="0.001"
            onkeyup="value=value.replace(/[^\d.]/g,'')"
            :disabled="train_disable"/>
        </form>
        <div class="more_info">
          <img class="question" id="lr_ques" src="../assets/问号.png">
          <div id="lr_detail">
            <div class="detail_title">
              Learning Rate
            </div>
            <div class="detail_content">
              Be careful tweaking this number! Even small differences can have huge effects on how well your model learns.
            </div>
          </div>
        </div>
      </div>
      <!-- 重置参数 -->
      <div id="reset_div">
        <div id="reset_text">Reset Default</div>
        <button id="reset_btn" @click="reset_params()"></button>
      </div>
    </div>
    <div id="preview">
      <div id="export_btn_div">
        <div id="pre_text" >Preview</div>
        <button id="export_model_btn" type="button" :disabled="export_disable" @click="showpopup()">Export Model</button>
      </div>
      <div id="choose_div">
        <div id="exchange">
          <el-switch
            id="web-file"
            @change="changeMode('web-file')"
            v-model="is_cam"
            active-text="Webcam"
            :disabled="export_disable"
            inactive-text="Upload">
          </el-switch>
        </div>
        <div class="choose-box" v-show="is_cam">
          <video class="webcam-display1" id="_video"></video>
          <button class="b2" @click="setImage3()" :disabled="export_disable">Photograph</button>
          <canvas hidden="hidden" class="canvas-display1" id="_canvas"   width="1280px" height="720px"></canvas>
          <img id="img-wrapper4">
        </div>
        <div class="choose-box" v-show="!is_cam">
          <div class="img-wrapper">
            <img id="img-wrapper3">
          </div>
          <div class="upload_btn_div1">
            <button
            class="upload_btn"
            @click="change_input($event)"
            id="btn3"
            :disabled="export_disable">
            Upload Images
            </button>
            <form @change="setImg($event)">
              <input id="fileOne" type="file" name="image" accept = 'image/jpeg,image/jpg,image/png,image/bmp'/>
            </form>
          </div>
          <div id="predict_ex">
            <div class="img_div">
              <img src="../assets/图片2.png" class="file-box-imgs">
              <img src="../assets/箭头.png" class="file-box-imgs">
              <img src="../assets/图片2.png" class="file-box-imgs">
              <div class="crop_size"></div>
            </div>
            <div class="crop_decript">Images will be cropped to square</div>
          </div>
        </div>
        <div id="pre_btn_div">
          <button id="pre_btn" @click="prediction()" :disabled="predict_disable">Predict</button>
        </div>
      </div>
      <div id="progress_div">
        <span class="class-text">Output</span>
        <div class="pre_outcome">
          <div id="class_text1">{{ label1_value }}:</div>
          <div class="Bar1">
            <div id="orange1">
              <div id="orangename1">0%</div>
            </div>
          </div>
        </div>
        <div class="pre_outcom">
          <div id="class_text2">{{ label2_value }}:</div>
          <div class="Bar2">
            <div id="orange2">
              <div id="orangename2">0%</div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="all" v-show="popup">
      <!--这里是要展示的内容层-->
      <div class="login">
        <el-tabs type="border-card">
          <el-tab-pane label="Tensorflow">
            <div class="text11">
              <button class="download_btn" type="button" @click="exportModel('h5')">Download my model</button>
              <div class="text1" onselectstart="javascript:return false;">
                Converts your model to a kera .h5 model. Note the conversion happens in the cloud, but your training data is not being uploaded, only your trained model.
              </div>
              <div class="text2" onselectstart="javascript:return false;">
                Code snippets to use your model:
              </div>
              <div class="text3">
                <br>
                &nbsp;&nbsp;import tensorflow.keras
                <br>
                &nbsp;&nbsp;from PIL import Image, ImageOps
                <br>
                &nbsp;&nbsp;import numpy as np
                <br><br>

                &nbsp;&nbsp;# Disable scientific notation for clarity<br>
                &nbsp;&nbsp;np.set_printoptions(suppress=True)<br><br>

                &nbsp;&nbsp;# Load the model<br>
                &nbsp;&nbsp;model = tensorflow.keras.models.load_model('my_model.h5')<br><br>

                &nbsp;&nbsp;# Create the array of the right shape to feed into the keras model<br>
                &nbsp;&nbsp;# The 'length' or number of images you can put into the array is<br>
                &nbsp;&nbsp;# determined by the first position in the shape tuple, in this case 1.<br>
                &nbsp;&nbsp;data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)<br><br>

                &nbsp;&nbsp;# Replace this with the path to your image<br>
                &nbsp;&nbsp;image = Image.open('test_photo.jpg')<br><br>

                &nbsp;&nbsp;#resize the image to a 224x224 with the same strategy as in TM2:<br>
                &nbsp;&nbsp;#resizing the image to be at least 224x224 and then cropping from the center<br>
                &nbsp;&nbsp;size = (224, 224)<br>
                &nbsp;&nbsp;image = ImageOps.fit(image, size, Image.ANTIALIAS)<br><br>

                &nbsp;&nbsp;#turn the image into a numpy array<br>
                &nbsp;&nbsp;image_array = np.asarray(image)<br><br>

                &nbsp;&nbsp;# display the resized image<br>
                &nbsp;&nbsp;image.show()<br><br>

                &nbsp;&nbsp;# Normalize the image<br>
                &nbsp;&nbsp;normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1<br><br>

                &nbsp;&nbsp;# Load the image into the array<br>
                &nbsp;&nbsp;data[0] = normalized_image_array<br><br>

                &nbsp;&nbsp;# run the inference<br>
                &nbsp;&nbsp;prediction = model.predict(data)<br>
                &nbsp;&nbsp;print(prediction)<br><br>
              </div>
              <div>
              <button
                class="quite_btn"
                @click="closepopup">
                Close
              </button>
              </div>
            </div>
          </el-tab-pane>
          <el-tab-pane label="Tensorflow Lite">
            <div class="text11">
              <button class="download_btn" type="button" @click="exportModel('tflite')">Download my model</button>
              <div class="text1" onselectstart="javascript:return false;">
                Convert your model to a tflite floating point model. Note the conversion happens in the cloud, but your training data is not being uploaded, only your trained model.
              </div>
              <div class="text2" onselectstart="javascript:return false;">
                Code snippets to use your model:
              </div>
              <div class="text3">
                <br>
                &nbsp;The TFLite mobilenet example works with the teachable machine model.
                <br><br>
                &nbsp;1. Get the project from <a href="https://github.com/tensorflow/examples/tree/master/lite/examples/image_classification/android" target="_blank">github</a>
                <br><br>
                &nbsp;2. Put your downloadmodel into app/src/assets
                <br><br>

                &nbsp;3. Create/update labels.txt in app/src/assets<br><br>
                &nbsp;4. Change the default model type in CameraActivity.java in android/app/src/main/java/org/tensorflow/lite/examples/classfication/<br><br>

                &nbsp;from <br><br>
                &nbsp;&nbsp;&nbsp;&nbsp;private Model model = Model.QUANTIZED;<br><br>

                &nbsp;to<br><br>
                &nbsp;&nbsp;&nbsp;&nbsp;private Model model = Model.FLOAT;<br><br>
                &nbsp;5. Change ClasffierFloatMobileNet.java in android/app/src/main/java/org/tensorflow/lite/examples/classification/tflite/<br><br>
                &nbsp;from<br><br>

                &nbsp;&nbsp;&nbsp;&nbsp;return "mobilenet_v1_1.0_224.tflite";<br><br>
                &nbsp;to<br><br>

                &nbsp;&nbsp;&nbsp;&nbsp;return "model_unquant.tflite";<br><br>
              </div>
              <div>
              <button
                class="quite_btn"
                @click="closepopup">
                Close
              </button>
              </div>
            </div>
          </el-tab-pane>
        </el-tabs>
      </div>
    </div>
  </div>
</template>

<style scoped>
  .all {
    position: fixed;
    width: 100%;
    height: 100%;
    filter: alpha(opacity=70);
    top: 0;
    left: 0;
    z-index: 999;
    background-color: rgba(193, 193, 193, 0.7);
    overflow-y: scroll;
  }
  .login {
    position: absolute;
    font-size: 24px;
    height: 600px;
    width: 700px;
    background-color: white;
    border-radius: 0.25rem;
    left: 50%;
    top: 55%;
    transform: translate(-50%, -50%);
    z-index: 1111;
  }
  .download_btn{
    background-color: #b4d8ff;
    border: none;
    width: 200px;
    height: 30px;
    position: relative;
    top: 5px;
    left: -223px;
    border-radius: 10px;
    color: #4289d6;
    font-weight: bold;
    font-size: 16px;
    transition: 0.5s;
  }
  .text1{
    position: relative;
    top: 20px;
    left: 5px;
    font-size: 14px;
    text-align:left;
    width: 96.5%;
  }
  .text11{
    position: relative;
    width: 670px;
    overflow-y: scroll;
    overflow-x: hidden;
  }
  .text2{
    position: relative;
    top: 30px;
    left: 5px;
    font-size: 15px;
    text-align:left;
    font-weight: bold;
    width: 96.5%;
  }
  .text3{
    position: relative;
    top: 40px;
    left: 5px;
    font-size: 12px;
    text-align:left;
    color: #4289d6;
    background-color: #d5e9ff;
    border-radius: 10px;
    width: 96.5%;
  }
  .quite_btn{
    background-color: #b4d8ff;
    border: none;
    width: 100px;
    height: 30px;
    border-radius: 10px;
    color: #4289d6;
    font-weight: bold;
    font-size: 16px;
    position: relative;
    top: 50px;
    left: 5px;
  }

  input::-webkit-outer-spin-button,input::-webkit-inner-spin-button{
   -webkit-appearance: none !important;
  }
  input[type="number"]{-moz-appearance:textfield;}
  .upload_file{
    width: 0;
    height: 0;
  }
  #user-id{
    position: relative;
    left: 20px;
    width: 300px;
    height: 30px;
  }
  #input-id{
    float: left;
    width: 200px!important;
    height: 30px;
  }
  #check-id-btn{
    float: right;
    position: relative;
    top: 2px;
    font-size: 10px;
    font-weight: bold;
  }
  .Bar1{
    position: relative;
    width: 200px;
    border: 1px solid orange;
    padding: 1px;
    background-color: #ffebd3;
    border-radius: 8px;
    top: 50px;
    left: 30px;
  }
  #orange1{
    width: 0%;
    display: block;
    position: relative;
    background-color:#ff8c00;
    height: 20px;
    border-radius: 8px;
  }
  #orangename1{
    position: relative;
    width: 35px;
    color: white;
    text-align: center;
    font-weight: bold;
    top: -1px;
  }

  .Bar2{
    position: relative;
    width: 200px;
    border: 1px solid orange;
    padding: 1px;
    background-color: #ffe9ec;
    border-radius: 8px;
    top: 65px;
    left: 30px;
  }
  #orange2{
    width: 0%;
    display: block;
    position: relative;
    background-color:#ff0022;
    height: 20px;
    border-radius: 8px;
  }
  #orangename2{
    color: white;
    position: relative;
    width: 35px;
    text-align: center;
    font-weight: bold;
    top: 2px;
  }

  .label-name /deep/ .el-input__inner {
    font-weight: bold;
    font-size: 20px;
    border-top: none;
    border-left: none;
    border-right: none;
    border-radius: 0;
  }
  .class-box{
    overflow: hidden;
    margin: 50px 20px 40px 20px;
    position: relative;
    background-color: white;
    width: 400px;
    height: 400px;
    border-radius: 10px;
  }
  .choose-show-box{
    width: 400px;
    height: 360px;
  }
  .mode-box{
    float: left;
    width: 200px;
    height: 360px;
  }
  .show-box{
    float: right;
    width: 200px;
    height: 360px;
  }
  .change-mode{
    margin: 5px 0 5px 0;
  }
  .webcam-box{
    background-color: #d5e9ff;
    width: 200px;
    height: 330px;
  }
  .file-box{
    background-color: #d5e9ff;
    width: 200px;
    height: 330px;
  }
  .mode-text{
    position: relative;
    float: left;
    left: 5px;
    top: 5px;
    color: #296fff;
    font-size: 12px;
    font-weight: bold;
  }
  .class-text{
    position: relative;
    float: left;
    left: 20px;
    top: 5px;
    color: grey;
    font-size: 20px;
    font-weight: bold;
  }
  .dropBox{
    position: relative;
    left: 19px;
    top: 30px;
    background-color: #b4d8ff;
    width:160px;
    height:100px;
    margin:0 0 0 0;
    border-radius: 10px;
  }
  .choose-box{
    position: relative;
    left: 23px;
    top: 30px;
    background-color: #d5e9ff;
    width:240px;
    height:400px;
    margin:0 0 0 0;
    border-radius: 10px;
  }
  .upload_btn_div{
    position: relative;
    top: 50px;
  }
  .upload_btn_div1{
    position: relative;
    top: -100px;
  }
  .upload_btn{
    cursor: pointer;
    width: 120px;
    height: 30px;
    position: relative;
    border-radius: 10px;
    background-color: #b4d8ff;
    border: none;
    color: #4289d6;
  }
  .upload_btn:disabled{
    cursor: not-allowed;
    background: #EDEDED;
    color: #bcbcbc;
  }
  button:hover{
    cursor: pointer;
  }
  button:focus{
    outline: none;
  }
  .folder_img{
    position: relative;
    left: -15px;
    top: 15px;
    width: 40px;
    height: 40px;
  }
  .drap-content{
    position: relative;
    top: 30px;
    font-size: 10px;
    font-weight: bold;
    color: #4289d6;
  }
  .show-description{
    text-align: left;
    padding-top: 3px;
    padding-left: 5px;
    margin: 5px 0 5px 0;
    height: 17px;
    font-size: 12px;
    color: #878585;
    font-weight: bold;
  }
  .img-wrapper{
    overflow-y: auto;
    width: 200px;
    height: 340px;
    text-align: left;
  }
  #img-wrapper3{
    position: relative;
    top: 60px;
    right: -45px;
    width: 150px;
    height: 150px;
    background-color: #d5e9ff;
    border-radius: 10px;
  }
  #img-wrapper4{
    position: relative;
    top: 70px;
    width: 150px;
    height: 150px;
    background-color: #d5e9ff;
    border-radius: 10px;
    border: none;
  }
  .file-box-imgs{
    margin-top: 3px;
    position: relative;
    width: 56px;
    height: 40px;
  }
  .crop_size{
    position: relative;
    left: 139px;
    bottom: 44.3px;
    height: 36.5px;
    width: 36.5px;
    border: 2px #2c3e50 solid;
  }
  .pre_img_decript{
    position: relative;
    top: 100px;
    width: 200px;
    height: 100px;
  }
  .crop_decript{
    position: relative;
    bottom: 35px;
    font-size: 11px;
    font-weight: bold;
    color: #4289d6;
  }
  #addTextForm{
    width: 0;
    height: 0;
  }
  .webcam-display{
    position: relative;
    top: 50px;
    right: 25px;
    width: 150px;
    height: 150px;
    background-color: #b4d8ff;
    border-radius: 10px;
  }
  .webcam-display1{
    position: relative;
    top: 30px;
    left: 40px;
    width: 150px;
    height: 150px;
    background-color: #b4d8ff;
    border-radius: 10px;
  }
  #setting{
    position: relative;
    bottom: 650px;
    left: 500px;
    width:200px;
    height:380px;
    background-color: white;
    border-radius: 20px;
  }
  #preview{
    position: relative;
    bottom: 1200px;
    left: 800px;
    width:300px;
    height:800px;
    background-color: white;
    border-radius: 20px;
  }
  #export_btn_div{
    width: 300px;
    height: 60px;
    border-bottom: 2px solid;
    border-bottom-color: #EDEDED;
  }
  #train_btn_div{
    width: 200px;
    height: 100px;
    border-bottom: 2px solid;
    border-bottom-color: #EDEDED;
  }
  #pre_text{
    position: relative;
    left: 10px;
    top: 10px;
    font-weight: bold;
    font-size: 24px;
    width: 100px;
  }
  #train_text{
    position: relative;
    left: 10px;
    top: 10px;
    font-weight: bold;
    font-size: 24px;
    width: 100px;
  }
  #export_model_btn{
    background-color: #b4d8ff;
    border: none;
    width: 120px;
    height: 30px;
    position: relative;
    top: -15px;
    left: 50px;
    border-radius: 10px;
    color: #4289d6;
    font-weight: bold;
    font-size: 16px;
    transition: 0.5s;
  }
  #export_model_btn:disabled{
    cursor: not-allowed;
    background: #EDEDED;
    color: #bcbcbc;
  }
  #train_model_btn{
    background-color: #b4d8ff;
    border: none;
    width: 120px;
    height: 30px;
    position: relative;
    top: 20px;
    border-radius: 10px;
    color: #4289d6;
    font-weight: bold;
    font-size: 16px;
    transition: 0.5s;
  }
  #train_model_btn:disabled{
    cursor: not-allowed;
    background: #EDEDED;
    color: #bcbcbc;
  }
  #epoch_div{
    width: 200px;
    height: 100px;
    border-bottom: 2px solid;
    border-bottom-color: #EDEDED;
  }
  #choose_div{
    width: 300px;
    height: 560px;
    border-bottom: 2px solid;
    border-bottom-color: #EDEDED;
  }
  #advance{
    color: #5974ff;
    width: 100px;
    text-align: left;
    position: relative;
    top: 10px;
    left: 10px;
  }
  #epoch_form{
    position: relative;
    top: 20px;
    left: 10px;
    text-align: left;
  }
  #epochs{
    width: 40px;
  }
  #batch_div{
    width: 200px;
    height: 50px;
    border-bottom: 2px solid;
    border-bottom-color: #EDEDED;
  }
  #batch_form{
    text-align: left;
    position: relative;
    left: 10px;
    top: 15px;
  }
  #lr_div{
    width: 200px;
    height: 70px;
    border-bottom: 2px solid;
    border-bottom-color: #EDEDED;
  }
  #lr_form{
    text-align: left;
    position: relative;
    left: 10px;
    top: 15px;
  }
  #learning_rate{
    position: relative;
    top: 5px;
  }
  .train_info{
    width: 50px;
    color: #082CF8;
    padding-left: 5px;
    padding-top: 3px;
    padding-bottom: 3px;
    background-color: #d5e9ff;
    border:none;
    border-radius: 5px;
  }
  .train_info:disabled{
    background-color: #EDEDED;
    color: #bcbaba;
  }
  #exchange{
    position: relative;
    top:10px;
  }

  #reset_text{
    font-weight: bold;
    color: #bebcbc;
    position: relative;
    left: 10px;
    top: 15px;
    width: 130px;
    text-align: left;
  }
  #class_text1{
    font-weight: bold;
    color: #b4d8ff;
    position: relative;
    text-align: left;
    right: 45px;
    top: 40px;
    max-width: 280px;
  }
  #class_text2{
    font-weight: bold;
    color: #b4d8ff;
    position: relative;
    text-align: left;
    left: 20px;
    top: 60px;
    max-width: 280px;
  }
  #reset_btn{
    background-image: url("../assets/重置.png");
    background-color: white;
    background-size: cover;
    width: 24px;
    height: 24px;
    border:none;
    float: right;
    position: relative;
    bottom: 8px;
    right: 10px;
  }
  .question{
    width: 20px;
    height: 20px;
    float: right;
    position: relative;
    right: 10px;
    cursor: pointer;
  }
  #epo_ques{
    z-index: 101;
    bottom: 10px;
  }
  #epo_ques:hover+#epo_detail{
    z-index: 100;
    opacity: 0.85;
  }
  #bat_ques{
    z-index: 99;
    bottom: 16px;
  }
  #bat_ques:hover+#bat_detail{
    z-index: 98;
    opacity: 0.85;
  }
  #lr_ques{
    z-index: 97;
    bottom: 10px;
  }
  #lr_ques:hover+#lr_detail{
    z-index: 96;
    opacity: 0.85;
  }
  #epo_detail{
    border-radius: 10px;
    position:relative;
    right: 109px;
    bottom: 21px;
    width: 300px;
    height: 350px;
    background-color: black;
    z-index: -1;
    opacity: 0;
    text-align: left;
  }
  .detail_title{
    padding-left: 10px;
    padding-top: 10px;
    color: white;
    font-weight: bold;
    margin: 10px 0 10px 0;
  }
  .detail_content{
    padding-right: 50px;
    padding-left: 10px;
    color: white;
  }
  #bat_detail{
    border-radius: 10px;
    position:relative;
    right: 109px;
    bottom: 27px;
    width: 300px;
    height: 320px;
    background-color: black;
    z-index: -1;
    opacity: 0;
    text-align: left;
  }
  #lr_detail{
    border-radius: 10px;
    position:relative;
    right: 109px;
    bottom: 30px;
    width: 300px;
    height: 130px;
    background-color: black;
    z-index: -1;
    opacity: 0;
    text-align: left;
  }
  .canvas-display{
    position: relative;
    top: -80px;
    right: 25px;
    width: 1280px;
    height: 720px;
    background-color: #b4d8ff;
  }
  .canvas-display1{
    position: relative;
    top: 80px;
    right: 0px;
    width: 1280px;
    height: 720px;
    background-color: #b4d8ff;
    border-radius: 10px;
  }
  .b1{
    position: relative;
    top: 100px;
    right: 0px;
    width: 130px;
    height: 30px;
    background-color: #b4d8ff;
    text-align: center;
    border-radius: 10px;
    cursor: pointer;
    border: none;
    color: #4289d6;
  }
  .b2{
    position: relative;
    top: 60px;
    right: 75px;
    width: 80px;
    height: 30px;
    background-color: #b4d8ff;
    text-align: center;
    border-radius: 10px;
    cursor: pointer;
    border: none;
    color: #4289d6;
  }
  .b2:disabled{
    cursor: not-allowed;
    background: #EDEDED;
    color: #bcbcbc;
  }
  #fileOne{
    display:none;
  }
  #predict_ex{
    position: relative;
    bottom: 60px;
    left: 20px;
    width: 200px;
    height: 100px;
  }
  #progress_div{
    width: 300px;
    height: 200px;
  }
  .pre_outcome{
    width: 300px;
    height: 50px;
  }
  #pre_btn_div{
    width: 300px;
    position: relative;
    top: 60px;
  }
  #pre_btn{
    background-color: #b4d8ff;
    border: none;
    width: 200px;
    height: 40px;
    position: relative;
    border-radius: 15px;
    color: #4289d6;
    font-weight: bold;
    font-size: 20px;
    transition: 0.5s;
  }
  #pre_btn:disabled{
    cursor: not-allowed;
    background: #EDEDED;
    color: #bcbcbc;
  }
</style>

<script>
import axios from 'axios'

/**
 base64格式转file
**/
function base64ToFile (base64Data, fileName) {
  let arr = base64Data.split(',')
  let mime = arr[0].match(/:(.*?);/)[1]
  let bytes = atob(arr[1]) // 解码base64
  let n = bytes.length
  let ia = new Uint8Array(n)
  while (n--) {
    ia[n] = bytes.charCodeAt(n)
  }
  return new File([ia], fileName, { type: mime })
}

/**
 判断拉进来的是不是图片
**/
function isImage (type) {
  switch (type) {
    case 'image/jpeg':
    case 'image/png':
    case 'image/bmp':
    case 'image/jpg':
      return true
    default:
      return false
  }
}

function get_valid_files (all_files, valid_index) {
  let arr2 = []
  for (let i = 0; i < valid_index.length; i++) {
    arr2.push(all_files[valid_index[i]])
  }
  return arr2
}

function get_valid_indexs (imgsTag) {
  let valid_index = []
  for (let i = 0; i < imgsTag.length; i++) {
    valid_index.push(imgsTag[i].id.split('_')[1])
  }
  return valid_index
}

export default {
  name: 'accident',
  // 定义数据
  data () {
    return {
      user_ID: '', // 用于多用户标识
      check_ID_pass: false, // ID是否有重复
      class1_input_index: 0, // class1的input照片下标
      class2_input_index: 0, // class2的input照片下标
      class1_input_file: [], // class1的input照片全部文件（包含删除的）
      class2_input_file: [], // class2的input照片全部文件（包含删除的）
      class1_drop_index: 0, // class1的drop照片下标
      class2_drop_index: 0, // class2的drop照片下标
      class1_drop_file: [], // class1的drop照片全部文件（包含删除的）
      class2_drop_file: [], // class2的drop照片全部文件（包含删除的）
      class1_web_index: 0,
      class2_web_index: 0,
      class1_web_file: [], // class1的web照片全部文件（包含删除的）
      class2_web_file: [], // class2的web照片全部文件（包含删除的）
      is_camera1: false, // class1切换拍照或者本地选择
      is_camera2: false, // class2切换拍照或者本地选择
      is_cam: false,
      label1_value: 'Class1', // 类别1名称
      label2_value: 'Class2', // 类别2名称
      train_disable: true, // 控制训练按钮是否可用
      export_disable: true, // 控制导出按钮是否可用
      predict_disable: true, // 控制预测按钮是否可用
      imgSrc1: '',
      imgSrc2: '',
      thisCancas1: null,
      thisCancas2: null,
      thisContext1: null,
      thisContext2: null,
      thisVideo1: null,
      thisVideo2: null,
      imgSrc: '',
      thisCancas: null,
      thisContext: null,
      thisVideo: null,
      class1_orange: 0,
      class2_orange: 0,
      class1_orangename: null,
      class2_orangename: null,
      predict_upload_file: null,
      predict_web_file: null,
      waiting_display: false,
      export_type: '',
      popup: false,
      can_clear: true
    }
  },
  // 定义事件
  methods: {
    changeMode (e) {
      if (e === 'web-file') {
        this.is_camera1 = false
        this.is_camera2 = false
      } else if (e === 'class1-change') {
        this.is_cam = false
        this.is_camera2 = false
      } else if (e === 'class2-change') {
        this.is_cam = false
        this.is_camera1 = false
      }
    },
    // 检查用户ID是否可用
    checkID () {
      const path = 'http://127.0.0.1:5000/CheckID'
      if (this.user_ID === '') {
        alert('ERROR! Please enter User ID.')
      } else {
        let uploaddata = new FormData()// 创建form对象
        uploaddata.append('userID', this.user_ID)
        axios.post(path, uploaddata)
          .then((res) => {
            if (res.data === 'FALSE') {
              alert('ERROR! The ID you entered already exists.')
            } else if (res.data === 'TRUE') {
              this.check_ID_pass = true
            }
          })
          .catch((error) => {
            console.error(error)
          })
      }
    },

    showpopup () {
      this.popup = true
    },

    closepopup () {
      this.popup = false
    },
    // 导出模型倒本地
    exportModel (e) {
      this.can_clear = false
      this.export_type = e
      let loading = this.$loading({
        lock: true,
        text: 'Please wait......',
        spinner: 'el-icon-loading',
        background: 'rgba(0, 0, 0, 0.7)'
      })
      const model_path = 'http://127.0.0.1:5000/modelExport'
      let uploaddata = new FormData()// 创建form对象
      uploaddata.append('userID', this.user_ID)
      uploaddata.append('model_type', this.export_type)
      uploaddata.append('label1', this.label1_value)
      uploaddata.append('label2', this.label2_value)
      let config = {responseType: 'blob'}
      axios.post(model_path, uploaddata, config)
        .then((res) => {
          console.log(res)
          let blob = new Blob([res.data], {type: 'application/octet-stream'})
          let url = window.URL.createObjectURL(blob)
          let a = document.createElement('a')
          a.href = url
          if (this.export_type === 'h5') {
            a.download = 'my_model.h5'
          } else if (this.export_type === 'tflite') {
            a.download = 'my_model.tflite'
          }
          a.click()
          window.URL.revokeObjectURL(url)
          loading.close()
        })
        .catch((error) => {
          console.error(error)
        })
      const label_path = 'http://127.0.0.1:5000/labelExport'
      axios.post(label_path, uploaddata, config)
        .then((res) => {
          console.log(res)
          let blob = new Blob([res.data], {type: 'application/octet-stream'})
          let url = window.URL.createObjectURL(blob)
          let a = document.createElement('a')
          a.href = url
          a.download = 'labels.txt'
          a.click()
          window.URL.revokeObjectURL(url)
        })
        .catch((error) => {
          console.error(error)
        })
      this.can_clear = true
    },
    // 预测
    prediction () {
      let loading = this.$loading({
        lock: true,
        text: 'Please wait......',
        spinner: 'el-icon-loading',
        background: 'rgba(0, 0, 0, 0.7)'
      })
      const path = 'http://127.0.0.1:5000/imagesPrediction'
      // const path = 'http://192.168.1.112:5000/imagesPrediction'
      let uploaddata = new FormData()// 创建form对象
      if (this.is_cam === true) {
        uploaddata.append('predict_img', this.predict_web_file)
      } else {
        uploaddata.append('predict_img', this.predict_upload_file)
      }
      uploaddata.append('userID', this.user_ID)
      let config = {
        headers: {'Content-Type': 'multipart/form-data'}
      }
      axios.post(path, uploaddata, config)
        .then((res) => {
          console.log(res.data)
          let class1_pre = (res.data[0] * 100)
          let class2_pre = (res.data[1] * 100)
          let offset1 = 0
          let offset2 = 0
          if (class1_pre <= 20) {
            offset1 = 0
          } else {
            offset1 = 200 * (class1_pre / 100) - 40
          }
          if (class2_pre <= 20) {
            offset2 = 0
          } else {
            offset2 = 200 * (class2_pre / 100) - 40
          }
          let class1_display = document.getElementById('orangename1')
          let class2_display = document.getElementById('orangename2')
          class1_display.innerHTML = class1_pre + '%'
          $('#orangename1').css({'left': offset1})
          $('#orangename2').css({'left': offset2})
          class2_display.innerHTML = class2_pre + '%'
          $('#orange1').css({'width': class1_pre + '%'})
          $('#orange2').css({'width': class2_pre + '%'})
          loading.close()
        })
        .catch((error) => {
          console.error(error)
        })
    },
    // 检查输入和label是否满足可以训练的条件
    check_train () {
      let class1_input_imgs = document.getElementsByClassName('class1_input')
      let class2_input_imgs = document.getElementsByClassName('class2_input')
      let class1_drop_imgs = document.getElementsByClassName('class1_drop')
      let class2_drop_imgs = document.getElementsByClassName('class2_drop')
      let class1_web_imgs = document.getElementsByClassName('class1_web')
      let class2_web_imgs = document.getElementsByClassName('class2_web')
      let valid_input_index1 = get_valid_indexs(class1_input_imgs)
      let valid_input_index2 = get_valid_indexs(class2_input_imgs)
      let valid_drop_index1 = get_valid_indexs(class1_drop_imgs)
      let valid_drop_index2 = get_valid_indexs(class2_drop_imgs)
      let valid_web_index1 = get_valid_indexs(class1_web_imgs)
      let valid_web_index2 = get_valid_indexs(class2_web_imgs)
      return (valid_input_index1.length !== 0 || valid_drop_index1.length !== 0 || valid_web_index1.length !== 0) && (valid_input_index2.length !== 0 || valid_drop_index2.length !== 0 || valid_web_index2.length !== 0) && (this.label1_value !== '' && this.label2_value !== '')
    },
    label_change () {
      this.train_disable = !this.check_train()
    },
    // 根据点击上传按钮触发input
    change_input (e) {
      if (e.target.id === 'btn1') {
        return $('#upload_file1').click()
      } else if (e.target.id === 'btn2') {
        return $('#upload_file2').click()
      } else if (e.target.id === 'btn3') {
        return $('#fileOne').click()
      }
    },

    // 当input选择了图片的时候触发,将获得的src赋值到相对应的img
    setImg (e) {
      let target = e.target
      if (target.id === 'fileOne') {
        $('#img-wrapper3').attr('src', window.URL.createObjectURL(target.files[0]))
        this.predict_upload_file = target.files[0]
        this.predict_disable = false
      } else {
        for (var i = 0; i < target.files.length; i++) {
          let my_img = $('<img src="">')
          my_img.attr('src', window.URL.createObjectURL(target.files[i]))
          my_img.attr('name', target.files[i].name)
          my_img.css({'width': '50px', 'height': '50px', 'margin': '5px 5px 5px 5px'})
          if (target.id === 'upload_file1') {
            my_img.attr('id', 'imgInput1_' + this.class1_input_index)
            this.class1_input_index += 1
            my_img.attr('class', 'class1_input')
            $('#img-wrapper1').append(my_img)
            this.class1_input_file.push(target.files[i])
          } else if (target.id === 'upload_file2') {
            my_img.attr('id', 'imgInput2_' + this.class2_input_index)
            this.class2_input_index += 1
            my_img.attr('class', 'class2_input')
            $('#img-wrapper2').append(my_img)
            this.class2_input_file.push(target.files[i])
          }
        }
      }
      this.train_disable = !this.check_train()
    },
    // 点击图片删除该图片并清除相对的input
    deleteImg (e) {
      let target = e.target
      if (target.nodeName === 'IMG') {
        target.parentNode.removeChild(target)
      }
      this.train_disable = !this.check_train()
    },
    setImage1 () {
      // 点击，canvas画图
      this.thisContext1.drawImage(this.thisVideo1, 0, 0, 1280, 720)
      // 获取图片base64链接
      var image = this.thisCancas1.toDataURL('image/jpeg', 1)
      this.imgSrc1 = image
      this.$emit('refreshDataList', this.imgSrc1)
      let web_file = base64ToFile(this.imgSrc1, 'imgWeb1_' + this.class1_web_index + '.jpeg')
      let my_img = $('<img src="' + this.imgSrc1 + '">')
      my_img.attr('name', 'imgWeb_' + this.class1_web_index)
      my_img.css({'width': '50px', 'height': '50px', 'margin': '5px 5px 5px 5px'}) // 添加样式，由于vue的执行机制，页面加载的时候img标签还没有生成，直接写在style样式会不生效
      my_img.attr('class', 'class1_web')
      my_img.attr('id', 'imgWeb_' + this.class1_web_index)
      $('#img-wrapper1').append(my_img)
      this.class1_web_file.push(web_file)
      this.class1_web_index += 1
      this.train_disable = !this.check_train()
    },
    setImage2 () {
      // 点击，canvas画图
      this.thisContext2.drawImage(this.thisVideo2, 0, 0, 1280, 720)
      // 获取图片base64链接
      var image = this.thisCancas2.toDataURL('image/jpeg', 1)
      this.imgSrc2 = image
      this.$emit('refreshDataList', this.imgSrc2)
      let web_file = base64ToFile(this.imgSrc2, 'imgWeb2_' + this.class2_web_index + '.jpeg')
      let my_img = $('<img src="' + this.imgSrc2 + '">')
      my_img.attr('name', 'imgWeb_' + this.class2_web_index)
      my_img.css({'width': '50px', 'height': '50px', 'margin': '5px 5px 5px 5px'}) // 添加样式，由于vue的执行机制，页面加载的时候img标签还没有生成，直接写在style样式会不生效
      my_img.attr('class', 'class2_web')
      my_img.attr('id', 'imgWeb_' + this.class2_web_index)
      $('#img-wrapper2').append(my_img)
      this.class2_web_file.push(web_file)
      this.class2_web_index += 1
      this.train_disable = !this.check_train()
    },
    setImage3 () {
      // 点击，canvas画图
      this.thisContext.drawImage(this.thisVideo, 0, 0, 1280, 720)
      // 获取图片base64链接
      var image = this.thisCancas.toDataURL('image/jpeg', 1)
      this.imgSrc = image
      $('#img-wrapper4').attr('src', this.imgSrc)
      this.predict_web_file = base64ToFile(this.imgSrc, 'prediction.jpeg')
      this.$emit('refreshDataList', this.imgSrc)
      this.predict_disable = false
    },

    // 提交信息到后台
    submit () {
      let loading = this.$loading({
        lock: true,
        text: 'Training in backend, please wait......',
        spinner: 'el-icon-loading',
        background: 'rgba(0, 0, 0, 0.7)'
      })
      const path = 'http://127.0.0.1:5000/imagesTraining'
      // const path = 'http://192.168.1.112:5000/imagesTraining'
      let uploaddata = new FormData()// 创建form对象
      let class1_input_imgs = document.getElementsByClassName('class1_input')
      let class2_input_imgs = document.getElementsByClassName('class2_input')
      let class1_drop_imgs = document.getElementsByClassName('class1_drop')
      let class2_drop_imgs = document.getElementsByClassName('class2_drop')
      let class1_web_imgs = document.getElementsByClassName('class1_web')
      let class2_web_imgs = document.getElementsByClassName('class2_web')
      let valid_input_index1 = get_valid_indexs(class1_input_imgs)
      let valid_input_index2 = get_valid_indexs(class2_input_imgs)
      let valid_drop_index1 = get_valid_indexs(class1_drop_imgs)
      let valid_drop_index2 = get_valid_indexs(class2_drop_imgs)
      let valid_web_index1 = get_valid_indexs(class1_web_imgs)
      let valid_web_index2 = get_valid_indexs(class2_web_imgs)
      let valid_input_files1 = get_valid_files(this.class1_input_file, valid_input_index1)
      let valid_input_files2 = get_valid_files(this.class2_input_file, valid_input_index2)
      let valid_drop_files1 = get_valid_files(this.class1_drop_file, valid_drop_index1)
      let valid_drop_files2 = get_valid_files(this.class2_drop_file, valid_drop_index2)
      let valid_web_files1 = get_valid_files(this.class1_web_file, valid_web_index1)
      let valid_web_files2 = get_valid_files(this.class2_web_file, valid_web_index2)
      let class1_valid_imgs = valid_input_files1.concat(valid_drop_files1).concat(valid_web_files1)
      let class2_valid_imgs = valid_input_files2.concat(valid_drop_files2).concat(valid_web_files2)
      if (class1_valid_imgs.length === 0) {
        alert('ERROR! Please add Class1 image!')
      } else if (class2_valid_imgs.length === 0) {
        alert('ERROR! Please add Class2 image!')
      } else if (this.label1_value === '') {
        alert('ERROR! Please edit Class1 Name!')
      } else if (this.label2_value === '') {
        alert('ERROR! Please edit Class2 Name!')
      } else {
        for (let i = 0; i < class1_valid_imgs.length; i++) {
          uploaddata.append('label1_imgs', class1_valid_imgs[i])
        }
        for (let i = 0; i < class2_valid_imgs.length; i++) {
          uploaddata.append('label2_imgs', class2_valid_imgs[i])
        }
        let epoch = document.getElementById('epochs').value
        let batch = document.getElementById('batch').value
        let learningRate = document.getElementById('learning_rate').value
        uploaddata.append('label', this.label1_value)
        uploaddata.append('label', this.label2_value)
        uploaddata.append('epoch', epoch)
        uploaddata.append('batch', batch)
        uploaddata.append('learning_rate', learningRate)
        uploaddata.append('userID', this.user_ID)
        let config = {
          headers: {'Content-Type': 'multipart/form-data'}
        }
        axios.post(path, uploaddata, config)
          .then((res) => {
            loading.close()
            this.export_disable = false
          })
          .catch((error) => {
            loading.close()
            console.error(error)
            alert(error)
          })
      }
    },
    // 重置训练参数
    reset_params () {
      document.getElementById('epochs').value = 50
      document.getElementById('batch').value = 16
      document.getElementById('learning_rate').value = 0.001
    },
    // 离开或刷新的时候清除该用户文件夹
    async leave_func (e) {
      if (this.can_clear === true) {
        console.log('清理后台文件')
        const path = 'http://127.0.0.1:5000/leave'
        let uploaddata = new FormData()// 创建form对象
        uploaddata.append('userID', this.user_ID)
        await axios.post(path, uploaddata)
      }
    }
  },
  created () {
    // 绑定清除文件夹事件
    window.addEventListener('beforeunload', e => this.leave_func(e))
  },
  mounted () {
    let _this = this
    let flag = true
    $('#id-text').on('compositionstart', function () {
      flag = false
    })
    $('#id-text').on('compositionend', function () {
      flag = true
    })
    $('#id-text').on('input', function () {
      setTimeout(function () {
        if (flag) {
          _this.user_ID = _this.user_ID.replace(/[^A-Za-z0-9_\u4E00-\u9FA5]/g, '')
        }
      }, 0)
    })
    this.class1_orange = document.getElementById('orange1')
    this.class2_orange = document.getElementById('orange2')
    this.class1_orangename = document.getElementById('orangename1')
    this.class2_orangename = document.getElementById('orangename2')

    this.thisCancas1 = document.getElementById('class1_canvas')
    this.thisContext1 = this.thisCancas1.getContext('2d')
    this.thisVideo1 = document.getElementById('class1_video')
    this.thisCancas2 = document.getElementById('class2_canvas')
    this.thisContext2 = this.thisCancas2.getContext('2d')
    this.thisVideo2 = document.getElementById('class2_video')
    this.thisCancas = document.getElementById('_canvas')
    this.thisContext = this.thisCancas.getContext('2d')
    this.thisVideo = document.getElementById('_video')

    if (navigator.mediaDevices.getUserMedia) {
      // 最新的标准API
      navigator.mediaDevices.getUserMedia({video: {width: 1280, height: 720}}).then(success).catch(error)
    } else if (navigator.webkitGetUserMedia) {
      // webkit核心浏览器
      navigator.webkitGetUserMedia({video: {width: 1280, height: 720}}, success, error)
    } else if (navigator.mozGetUserMedia) {
      // firfox浏览器
      navigator.mozGetUserMedia({video: {width: 1280, height: 720}}, success, error)
    } else if (navigator.getUserMedia) {
      // 旧版API
      navigator.getUserMedia({video: {width: 1280, height: 720}}, success, error)
    }

    function success (stream) {
      // 兼容webkit核心浏览器
      // let CompatibleURL = window.URL || window.webkitURL;

      // 将视频流设置为video元素的源
      console.log(stream)

      // video.src = CompatibleURL.createObjectURL(stream);
      _this.thisVideo1.srcObject = stream
      _this.thisVideo1.play()
      _this.thisVideo2.srcObject = stream
      _this.thisVideo2.play()
      _this.thisVideo.srcObject = stream
      _this.thisVideo.play()
    }

    function error (error) {
      alert(`访问用户媒体设备失败${error.name}, ${error.message}`)
    }

    var __this = this
    /*
    拖拽事件监听========================================
    */
    var Boxed = document.getElementsByClassName('dropBox')
    for (var i = 0; i < Boxed.length; i++) {
      Boxed[i].addEventListener('dragover', function (e) {
        e.stopPropagation()
        e.preventDefault()
      }, false)
      Boxed[i].addEventListener('drop', handleDrop, false)
    }
    function handleDrop (evt) {
      evt.stopPropagation()
      evt.preventDefault()
      var files = evt.dataTransfer.files
      for (var i = 0; i < files.length; i++) {
        let f = files[i]
        var t = f.type ? f.type : 'n/a'
        var reader = new FileReader()
        var isImg = isImage(t)
        // 处理得到的图片
        if (isImg) {
          reader.onload = (function (theFile) {
            return function (e) {
              let drop_file = base64ToFile(e.target.result, theFile.name)
              let my_img = $('<img src="' + e.target.result + '">')
              my_img.attr('name', theFile.name)
              my_img.css({'width': '50px', 'height': '50px', 'margin': '5px 5px 5px 5px'}) // 添加样式，由于vue的执行机制，页面加载的时候img标签还没有生成，直接写在style样式会不生效
              if (evt.target.id === 'dropBox1') {
                my_img.attr('class', 'class1_drop')
                my_img.attr('id', 'imgDrop1_' + __this.class1_drop_index)
                $('#img-wrapper1').append(my_img)
                __this.class1_drop_file.push(drop_file)
                __this.class1_drop_index += 1
              } else if (evt.target.id === 'dropBox2') {
                my_img.attr('class', 'class2_drop')
                my_img.attr('id', 'imgDrop2_' + __this.class2_drop_index)
                $('#img-wrapper2').append(my_img)
                __this.class2_drop_file.push(drop_file)
                __this.class2_drop_index += 1
              }
              __this.train_disable = !__this.check_train()
            }
          })(f)
          reader.readAsDataURL(f)
        } else {
          alert('Please only drop image type files!')
        }
      }
    }
  },
  destroyed () {
    // 卸载清除文件夹事件
    window.removeEventListener('beforeunload', e => this.leave_func(e))
  }
}
</script>
