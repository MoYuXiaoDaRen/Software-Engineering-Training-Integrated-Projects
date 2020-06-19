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
            v-model="is_camera"
            active-text="摄像头上传"
            inactive-text="本地上传">
          </el-switch>
          <div class="webcam-box" v-show="is_camera">
            <span class="mode-text">Webcam</span>
            <video id="video" :width="videoWidth" :height="videoHeight" v-show="!imgSrc"></video>
            <canvas id="canvas" :width="videoWidth" :height="videoHeight" v-show="imgSrc"></canvas>
            <el-button type="primary" @click="setImage" v-if="!imgSrc" class="camera-btn">拍照</el-button>


          </div>
          <div class="file-box" v-show="!is_camera">
            <span class="mode-text">Files</span>
            <div class="dropBox" id="dropBox1">
              <img src="../assets/文件.png" id="folder_img">
              <div class="drap-content">Drag images file from your files</div>
            </div>
          </div>
        </div>
      </div>
      <div class="img-wrapper" id="img-wrapper" @click="deleteImg($event)"></div>
    </div>
      <div class="wrapper">
        <el-button type="primary" @click="change_input()">上传照片</el-button>
        <el-button type="primary" v-bind:disabled="is_disable">test</el-button>
        <form id="addTextForm" @change="setImg($event)">
        </form>
      </div>
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
  #folder_img{
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
  .camera-btn {
    margin-top: 20px;
  }
</style>

<script>
import {setFileUpload, deleteFileUpload, addUserCard } from "@/api/houseApi";

/**
 从 file 域获取 本地图片 url
**/
function getFileUrl (obj) {
  let url
  url = window.URL.createObjectURL(obj.files.item(0))
  return url
}

/**
 判断拉进来的是不是图片
**/
function isImage (type) {
  switch (type) {
    case 'image/jpeg':
    case 'image/png':
    case 'image/gif':
    case 'image/bmp':
    case 'image/jpg':
      return true
    default:
      return false
  }
}

export default {
  name: 'accident',
  props: {
      //【必选】CameraDialog弹窗显示状态
    show: {type: Boolean}
  },
  // 定义数据
  data () {
    return {
      imgNum: 0, // 上传的照片数量，可根据实际情况自定义
      is_disable: true,
      show3: false,
      is_camera: false, // 切换拍照或者本地选择
      label1_value: 'Class1', // 类别1名称
      label2_value: 'Class2', // 类别2名称
      thisCancas: null,
      thisContext: null,
      thisVideo: null,
      imgSrc: ``,
      videoWidth: '200',
      videoHeight: '330'
    }
  }, // 定义事件
  methods: {
    getCompetence() {
      var _this = this
      this.thisCancas = document.getElementById('canvas')
      this.thisContext = this.thisCancas.getContext('2d')
      this.thisVideo = document.getElementById('video')
      // 旧版本浏览器可能根本不支持mediaDevices，我们首先设置一个空对象
        if (navigator.mediaDevices === undefined) {
        navigator.mediaDevices = {}
      }
        // 一些浏览器实现了部分mediaDevices，我们不能只分配一个对象
        // 使用getUserMedia，因为它会覆盖现有的属性。
        // 这里，如果缺少getUserMedia属性，就添加它。
      if (navigator.mediaDevices.getUserMedia === undefined) {
        navigator.mediaDevices.getUserMedia = function (constraints) {
            // 首先获取现存的getUserMedia(如果存在)
          var getUserMedia = navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.getUserMedia
            // 有些浏览器不支持，会返回错误信息
            // 保持接口一致
          if (!getUserMedia) {
            return Promise.reject(new Error('getUserMedia is not implemented in this browser'))
          }
            // 否则，使用Promise将调用包装到旧的navigator.getUserMedia
          return new Promise(function (resolve, reject) {
            getUserMedia.call(navigator, constraints, resolve, reject)
          })
        }
      }
      var constraints = {
        audio: false,
        video: {width: this.videoWidth, height: this.videoHeight, transform: 'scaleX(-1)'}
      }
      navigator.mediaDevices.getUserMedia(constraints).then(function (stream) {
          // 旧的浏览器可能没有srcObject
        if ('srcObject' in _this.thisVideo) {
          _this.thisVideo.srcObject = stream
        } else {
            // 避免在新的浏览器中使用它，因为它正在被弃用。
          _this.thisVideo.src = window.URL.createObjectURL(stream)
        }
        _this.thisVideo.onloadedmetadata = function (e) {
          _this.thisVideo.play()
        }
      }).catch(err => {
        console.log(err)
      })
    },

    setImage() {
      var _this = this
        // 点击，canvas画图
      _this.thisContext.drawImage(_this.thisVideo, 0, 0, _this.videoWidth, _this.videoHeight)
        // 获取图片base64链接
      var image = this.thisCancas.toDataURL('image/png')
      _this.imgSrc = image
        // console.log(_this.imgSrc)
        // this.$emit('refreshDataList', this.imgSrc)
    },
      /*

    dataURLtoFile(dataurl, filename) {
      var arr = dataurl.split(',')
      var mime = arr[0].match(/:(.*?);/)[1]
      var bstr = atob(arr[1])
      var n = bstr.length
      var u8arr = new Uint8Array(n)
      while (n--) {
        u8arr[n] = bstr.charCodeAt(n)
      }
      return new File([u8arr], filename, {type: mime})
    },

    stopNavigator() {
      this.thisVideo.srcObject.getTracks()[0].stop()
    },

    // 刷新label输入值
    change_label (e) {
      this.$forceUpdate()
    },
    // 根据点击上传按钮触发input
    change_input () {
      this.is_disable = false
      this.imgNum += 1
      let my_input = $('<input type="file" name="image" />') // 创建一个input
      my_input.attr('id', this.imgNum) // 为创建的input添加id
      my_input.css({'width': '0px', 'height': '0px'})
      $('#addTextForm').append(my_input) // 将生成的input追加到指定的form

      let my_img = $('<img src="">')
      my_img.attr('id', 'img_' + this.imgNum)
      my_img.attr('class', 'class1')
      my_img.css({'max-width': '100px', 'max-height': '100px'}) // 添加样式，由于vue的执行机制，页面加载的时候img标签还没有生成，直接写在style样式会不生效
      $('#img-wrapper1').append(my_img)
      return my_input.click()

      let inputArr = $('#addTextForm input')
      let add_inputId = '' // 需要被触发的input
      for (let i = 0; i < inputArr.length; i++) {
        // 根据input的value值判断是否已经选择文件
        if (!inputArr[i].value) { // 如果没有选择,获得这个input的ID
          add_inputId = inputArr[i].id
          break
        }
      }
      if (add_inputId) { // 如果需要被触发的input ID存在,将对应的input触发
        return $('#' + add_inputId).click()
      } else {
        alert('最多选择' + this.imgNum + '张图片')
      }
    },
    // 当input选择了图片的时候触发,将获得的src赋值到相对应的img
    setImg (e) {
      let target = e.target
      $('#img_' + target.id).attr('src', getFileUrl(e.srcElement))
    },
    // 点击图片删除该图片并清除相对的input
    deleteImg (e) {
      let target = e.target
      let inputID = '' // 需要清除value的input
      if (target.nodeName == 'IMG') {
        target.src = ''
      }
    },
    // 提交信息到后台
    submit () {
      $('#addTextForm').ajaxSubmit({
        url: this.$root.api + '/Index/staff_accident/add',
        type: 'post',
        data: {
          'total_price': this.price,
          'descript': this.descript
        },
        success: (data) => {
          if (data.code == 0) {
            console.log('提交成功')
            $('#addTextForm input').val('')
            $('div#img-wrapper1 img').attr('src', '')
          } else {
            alert('提交失败')
          }
        }
      })
    }
  },
  mounted () {
    if (this.show) this.getCompetence()
    /*
    拖拽事件监听========================================
    */
    var oDropBox = document.getElementById('dropBox1')
    var imgwrapper = document.getElementById('img-wrapper1')
    oDropBox.addEventListener('dragover', function (e) {
      e.stopPropagation()
      e.preventDefault()
    }, false)
    oDropBox.addEventListener('drop', handleDrop, false)
    function handleDrop (evt) {
      evt.stopPropagation()
      evt.preventDefault()
      var files = evt.dataTransfer.files
      for (var i = 0, f; f = files[i]; i++) {
        console.log(f)
        console.log("Hello")
        var t = f.type ? f.type : 'n/a',
          reader = new FileReader(),
          isImg = isImage(t),
          img

        // 处理得到的图片
        if (isImg) {
          reader.onload = (function (theFile) {
            return function (e) {
              this.imgNum += 1
              let my_img = $('<img src="' + e.target.result + '">')
              my_img.attr('id', 'img_' + this.imgNum)
              my_img.attr('class', 'class1')
              my_img.css({'max-width': '100px', 'max-height': '100px'}) // 添加样式，由于vue的执行机制，页面加载的时候img标签还没有生成，直接写在style样式会不生效
              $('#img-wrapper1').append(my_img)
            }
          })(f)
          reader.readAsDataURL(f)
        } else {
          img = '"o((>ω< ))o"，你传进来的不是图片！！'
          looks(f, img)
        }

      }
    }

  }
}
</script>
