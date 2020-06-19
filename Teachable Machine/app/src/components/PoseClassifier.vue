<template>
  <div v-title data-title="Pose Classifier">
    <div id = "class1" overflow:hidden>
      <h3>第一类照片</h3>
      <form id="class1-form" @change="setImg($event)">
        <input type="file" name="image" accept="image/jpeg" id='1'/>
        <br>
        <br>
        <img src="" id='img_1' class="pic" >
        <br>
        <br>
        <input type="file" name="image" accept="image/jpeg" id='2'/>
        <br>
        <br>
        <img src="" id='img_2' class="pic">
        <br>
        <br>
        类别名称：<input type="text" name="first-name" id="class_label1" value="class1"/>
      </form>
    </div>
    <div id = "class2">
      <h3>第二类照片</h3>
        <form id="class2-form" @change="setImg($event)">
        <input type="file" name="image" accept="image/jpeg" id='3'/>
        <br>
        <br>
        <img src="" id='img_3' class="pic">
        <br>
        <br>
        <input type="file" name="image" accept="image/jpeg" id='4'/>
        <br>
        <br>
        <img src="" id='img_4' class="pic">
        <br>
        <br>
        类别名称：<input type="text" name="second-name" id="class_label2" value="class2"/>
      </form>
    </div>
    <!-- Training模块样式 -->
    <div id="setting">
      <!-- Train Model按钮 -->
      <div class="bottom-line">
        <div style="font-weight: bold; font-size: 24px;">Training</div>
        <button type="button" @click="submit()">Train Model</button>
      </div>
      <!-- Epoch输入 -->
      <div class="bottom-line">
        <span style="color: #5974ff; ">Advanced</span>
        <br>
        <form>
          <span style="font-weight: bold">Epochs: </span>
          <input type="number" class="train_info" id="epochs" value="16" onkeyup="value=value.replace(/^(0+)|[^\d]+/g,'')"/>
        </form>
      </div>
      <!-- Batch size选择 -->
      <div class="bottom-line">
        <form>
          <span style="font-weight: bold">Batch Size: </span>
          <select class="train_info" id="batch">
            <option value ="25">25</option>
            <option value ="50">50</option>
            <option value="100">100</option>
            <option value="150">150</option>
          </select>
        </form>
      </div>
      <!-- Learning rate输入 -->
      <div class="bottom-line">
        <form>
          <span style="font-weight: bold">Learning rate: </span>
          <input type="number" class="train_info" id="learning_rate" value="0.001" onkeyup="value=value.replace(/[^\d.]/g,'')"/>
        </form>
      </div>
      <!-- 重置参数 -->
      <div>
        <span style="font-weight: bold; color: #bebcbc">Reset Default</span>
        <button id="reset_btn" @click="reset_params()"></button>
      </div>
    </div>
  </div>
</template>

<style scoped>
  input::-webkit-outer-spin-button,input::-webkit-inner-spin-button{
   -webkit-appearance: none !important;
  }
  input[type="number"]{-moz-appearance:textfield;}
  .pic{
    max-width: 200px;
    max-height: 200px;
  }
  #setting{
    width:200px;
    // height:100px;
    background-color: white;
    border-radius: 20px;
  }
  .bottom-line{
    border-bottom: 2px solid;
    border-bottom-color: #EDEDED;
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
  #reset_btn{
    background-image: url("../assets/重置.png");
    background-color: white;
    background-size: cover;
    width: 25px;
    height: 25px;
    border:none;
  }
</style>

<script>
import axios from 'axios'

/**
  * 从 file 域获取 本地图片 url
  */
function getFileUrl (obj) {
  let url
  url = window.URL.createObjectURL(obj.files.item(0))
  return url
}

export default {
  name: 'imagesClassifier',
  // 定义数据
  data () {
    return {
      imgNum: 4 // 上传的照片数量，可根据实际情况自定义
    }
  },
  methods: {
    // 当input选择了图片的时候触发,将获得的src赋值到相对应的img
    setImg (e) {
      let target = e.target
      $('#img_' + target.id).attr('src', getFileUrl(e.srcElement))
    },
    // 提交信息到后台
    submit () {
      const path = 'http://127.0.0.1:5000/imagesClassifier'
      // const path = 'http://192.168.1.112:5000/imagesClassifier'
      let isImgEnough = true
      let isLabelEnough = true
      for (let i = 1; i <= 4; i++) {
        if ($('#img_' + i).attr('src') === '') {
          isImgEnough = false
          break
        }
      }
      for (let i = 1; i <= 2; i++) {
        if (document.getElementById('class_label' + i.toString()).value === '') {
          isLabelEnough = false
          break
        }
      }
      if (isImgEnough === false && isLabelEnough === false) {
        alert('请完成照片的选择以及标签填写')
      } else if (isImgEnough === false && isLabelEnough === true) {
        alert('请完成照片的选择')
      } else if (isImgEnough === true && isLabelEnough === false) {
        alert('请完成标签的填写')
      } else {
        var uploaddata = new FormData()// 创建form对象
        for (let i = 1; i <= 4; i++) {
          let file = document.getElementById(i.toString()).files[0]
          uploaddata.append('img_' + i.toString(), file)
        }
        for (let i = 1; i <= 2; i++) {
          let label = document.getElementById('class_label' + i.toString()).value
          uploaddata.append('label_' + i.toString(), label)
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
  }
}
</script>
