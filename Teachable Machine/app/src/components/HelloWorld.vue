<template>
  <div id="accident">
    <div class="class-box" id="box1">
      <div class="label-box">
        <el-input
          class="label-name"
          id="label1"
          placeholder="请输入类别名"
          prefix-icon="el-icon-edit"
          v-model="label1_value"
          clearable>
        </el-input>
      </div>
      <div class="choose-show-box">
        <div class="mode-box">
          <el-switch
            class="change-mode"
            v-model="is_camera1"
            active-text="摄像头上传"
            inactive-text="本地上传">
          </el-switch>
          <div class="webcam-box" v-show="is_camera1">
            <span class="mode-text">Webcam</span>
            <video class="webcam-display" id="class1_video"></video>
          </div>
          <div class="file-box" v-show="!is_camera1">
            <span class="mode-text">Files</span>
            <div class="dropBox" id="dropBox1">
              <img src="../assets/文件.png" class="folder_img">
              <div class="drap-content">Drag images file from your files</div>
            </div>
            <div class="upload_btn_div">
              <button
              class="upload_btn"
              @click="change_input($event)"
              id="btn1">
              上传照片
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
          placeholder="请输入类别名"
          prefix-icon="el-icon-edit"
          v-model="label2_value"
          clearable>
        </el-input>
      </div>
      <div class="choose-show-box">
        <div class="mode-box">
          <el-switch
            class="change-mode"
            v-model="is_camera2"
            active-text="摄像头上传"
            inactive-text="本地上传">
          </el-switch>
          <div class="webcam-box" v-show="is_camera2">
            <span class="mode-text">Webcam</span>
            <video class="webcam-display" id="class2_video"></video>
          </div>
          <div class="file-box" v-show="!is_camera2">
            <span class="mode-text">Files</span>
            <div class="dropBox" id="dropBox2">
              <img src="../assets/文件.png" class="folder_img">
              <div class="drap-content">Drag images file from your files</div>
            </div>
            <div class="upload_btn_div">
              <button
              class="upload_btn"
              @click="change_input($event)"
              id="btn2">
              上传照片
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
      <input type='file' multiple id="upload_file1" accept = 'image/jpeg,image/jpg,image/png,image/bmp'/>
      <input type='file' multiple id="upload_file2" accept = 'image/jpeg,image/jpg,image/png,image/bmp'/>
    </form>
    <button @click="submit () ">上传</button>
  </div>
</template>

<style scoped>
  .label-name /deep/ .el-input__inner {
    font-weight: bold;
    font-size: 20px;
    border-top: none;
    border-left: none;
    border-right: none;
    border-radius: 0;
  }
  .class-box{
    margin: 50px 20px 40px 20px;
    position: relative;
    overflow: hidden;
    background-color: white;
    width: 400px;
    height: 400px;
    border-radius: 10px;
  }
  .choose-show-box{
    overflow: hidden;
    width: 400px;
    height: 360px;
  }
  .mode-box{
    float: left;
    overflow: hidden;
    width: 200px;
    height: 360px;
  }
  .show-box{
    float: right;
    overflow: hidden;
    width: 200px;
    height: 360px;
  }
  .change-mode{
    margin: 5px 0 5px 0;
  }
  .webcam-box{
    overflow: hidden;
    background-color: #d5e9ff;
    width: 200px;
    height: 330px;
  }
  .file-box{
    overflow: hidden;
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
  .upload_btn_div{
    position: relative;
    overflow: hidden;
    top: 50px;
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
  button:hover{
    cursor: hand;
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
    overflow: hidden;
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
    overflow: hidden;
  }
  .webcam-display{
    position: relative;
    top: 50px;
    right: 25px;
    width: 150px;
    height: 150px;
    background-color: #b4d8ff;
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
      class1_input_index: 0, // class1的input照片下标
      class2_input_index: 0, // class2的input照片下标
      class1_input_file: [], // class1的input照片全部文件（包含删除的）
      class2_input_file: [], // class2的input照片全部文件（包含删除的）
      class1_drop_index: 0, // class1的drop照片下标
      class2_drop_index: 0, // class2的drop照片下标
      class1_drop_file: [], // class1的drop照片全部文件（包含删除的）
      class2_drop_file: [], // class2的drop照片全部文件（包含删除的）
      is_camera1: false, // class1切换拍照或者本地选择
      is_camera2: false, // class2切换拍照或者本地选择
      label1_value: 'Class1', // 类别1名称
      label2_value: 'Class2' // 类别2名称
    }
  }, // 定义事件
  methods: {
    // 根据点击上传按钮触发input
    change_input (e) {
      if (e.target.id === 'btn1') {
        return $('#upload_file1').click()
      } else if (e.target.id === 'btn2') {
        return $('#upload_file2').click()
      }
    },
    // 当input选择了图片的时候触发,将获得的src赋值到相对应的img
    setImg (e) {
      let target = e.target
      for (var i = 0; i < target.files.length; i++) {
        let my_img = $('<img src="">')
        my_img.attr('src', window.URL.createObjectURL(target.files[i]))
        my_img.attr('name', target.files[i].name)
        my_img.css({'max-width': '50px', 'max-height': '50px', 'margin': '5px 5px 5px 5px'})
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
    },
    // 点击图片删除该图片并清除相对的input
    deleteImg (e) {
      let target = e.target
      if (target.nodeName === 'IMG') {
        target.parentNode.removeChild(target)
      }
    },
    // 提交信息到后台
    submit () {
      const path = 'http://127.0.0.1:5000/imagesClassifier'
      var uploaddata = new FormData()// 创建form对象
      let class1_input_imgs = document.getElementsByClassName('class1_input')
      let class2_input_imgs = document.getElementsByClassName('class2_input')
      let class1_drop_imgs = document.getElementsByClassName('class1_drop')
      let class2_drop_imgs = document.getElementsByClassName('class2_drop')
      let valid_input_index1 = get_valid_indexs(class1_input_imgs)
      let valid_input_index2 = get_valid_indexs(class2_input_imgs)
      let valid_drop_index1 = get_valid_indexs(class1_drop_imgs)
      let valid_drop_index2 = get_valid_indexs(class2_drop_imgs)
      let valid_input_files1 = get_valid_files(this.class1_input_file, valid_input_index1)
      let valid_input_files2 = get_valid_files(this.class2_input_file, valid_input_index2)
      let valid_drop_files1 = get_valid_files(this.class1_drop_file, valid_drop_index1)
      let valid_drop_files2 = get_valid_files(this.class2_drop_file, valid_drop_index2)
      let class1_valid_imgs = valid_input_files1.concat(valid_drop_files1)
      let class2_valid_imgs = valid_input_files2.concat(valid_drop_files2)
      // console.log('label1 No1 content: ', class1_valid_imgs[0])
      // console.log('label2 length: ', class2_valid_imgs.length)
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
          uploaddata.append('label1', class1_valid_imgs[i])
        }
        for (let i = 0; i < class2_valid_imgs.length; i++) {
          uploaddata.append('label2', class2_valid_imgs[i])
        }
        let epoch = document.getElementById('epochs').value
        let batch = document.getElementById('batch').value
        let learningRate = document.getElementById('learning_rate').value
        uploaddata.append('epoch', epoch)
        uploaddata.append('batch', batch)
        uploaddata.append('learning_rate', learningRate)
        let config = {
          headers: {'Content-Type': 'multipart/form-data'}
        }
        axios.post(path, uploaddata, config)
          .then((res) => {
            alert(res.data)
          })
          .catch((error) => {
            console.error(error)
          })
      }
    },
    // 重置参数
    reset_params () {
      document.getElementById('epochs').value = 16
      document.getElementById('batch').value = 25
      document.getElementById('learning_rate').value = 0.001
    }
  },
  mounted () {
    var video1 = document.getElementById('class1_video')
    var video2 = document.getElementById('class2_video')
    const IMAGE_SIZE = 50
    if (navigator.mediaDevices.getUserMedia) {
      // 最新的标准API
      navigator.mediaDevices.getUserMedia({video: {width: 1000, height: 1000}}).then(success).catch(error)
    } else if (navigator.webkitGetUserMedia) {
      // webkit核心浏览器
      navigator.webkitGetUserMedia({video: {width: 1000, height: 1000}}, success, error)
    } else if (navigator.mozGetUserMedia) {
      // firfox浏览器
      navigator.mozGetUserMedia({video: {width: 1000, height: 1000}}, success, error)
    } else if (navigator.getUserMedia) {
      // 旧版API
      navigator.getUserMedia({video: {width: 1000, height: 1000}}, success, error)
    }

    function success (stream) {
      // 兼容webkit核心浏览器
      // let CompatibleURL = window.URL || window.webkitURL;

      // 将视频流设置为video元素的源
      console.log(stream)

      // video.src = CompatibleURL.createObjectURL(stream);
      video1.srcObject = stream
      video1.width = IMAGE_SIZE
      video1.height = IMAGE_SIZE
      video1.play()
      video2.srcObject = stream
      video2.width = IMAGE_SIZE
      video2.height = IMAGE_SIZE
      video2.play()
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
      for (var i = 0, f; f = files[i]; i++) {
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
              my_img.css({'max-width': '50px', 'max-height': '50px', 'margin': '5px 5px 5px 5px'}) // 添加样式，由于vue的执行机制，页面加载的时候img标签还没有生成，直接写在style样式会不生效
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
            }
          })(f)
          reader.readAsDataURL(f)
        } else {
          alert('Please only drop image type files!')
        }
      }
    }
  }
}
</script>
