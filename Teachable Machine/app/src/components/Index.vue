<template>
  <div v-title data-title="HomePage">
  <h1 style="position: fixed; top: 0px">New Project</h1>
    <div id="project">
      <div class="wrapper" onclick="window.open('./ImageClassifier')" id="imageClassifier">
        <img src="../assets/sample1.jpg">
        <img src="../assets/sample2.jpg">
        <span class="subTitle">Image Project</span>
        <div class="context">
          <span class="subContext">Teach based on images, from</span>
          <span class="subContext">files or your webcam.</span>
        </div>
      </div>
      <div class="notClick_wrapper" onclick="window.open('./SoundClassifier')" id="soundClassifier">
        <img src="../assets/sample1 (1).jpg">
        <img src="../assets/sample2 (1).jpg">
        <span class="subTitle">Sound Project</span>
        <div class="context">
          <span class="subContext">Teach based on one-second-long</span>
          <span class="subContext">sounds, from your microphone.</span>
        </div>
      </div>
      <div class="notClick_wrapper" onclick="window.open('./PoseClassifier')" id="poseClassifier" disabled="isDisable">
        <img src="../assets/sample1 (2).jpg">
        <img src="../assets/sample2 (2).jpg">
        <span class="subTitle">Pose Project</span>
        <div class="context">
          <span class="subContext">Teach based on images, from</span>
          <span class="subContext">files or your webcam.</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Index',
  data () {
    return {
      isDisable: true
    }
  }
}
</script>

<style scoped>
  h1{
    font-size: 48px;
    font-weight: bold;
  }
  img{
    width: 100px;
    height: 100px;
    margin: 20px 10px 10px;
    transition: 0.5s;
  }
  #project{
    height: 400px;
    position: absolute;
    top: 120px;
  }
  .notClick_wrapper{
    background-color: white;
    border-radius: 20px;
    cursor: pointer;
    width: 270px;
    height: 270px;
    overflow: hidden;
    transition: 0.5s;
    position: relative;
    left: 30px;
    float: left;
    margin: 40px 30px;
    pointer-events: none;
  }
  .wrapper{
    background-color: white;
    border-radius: 20px;
    cursor: pointer;
    width: 270px;
    height: 270px;
    overflow: hidden;
    transition: 0.5s;
    position: relative;
    left: 30px;
    float: left;
    margin: 40px 30px;
  }
  .wrapper:hover{
    transform: scale(1.1);
    background-color: #d5e9ff;
  }
  .wrapper:hover img{
    transform: scale(1.2);
  }
  .wrapper:hover .subTitle{
    font-size: 26px;
    transform: translateX(-11px);
  }
  .wrapper:hover .context{
    font-size: 16px;
    transform: translateX(-11px);
  }
  .subTitle{
    display: block;
    font-size: 24px;
    font-weight: bold;
    transition: 0.5s;
    position: relative;
    width: 180px;
    text-align: left;
    left: 22px;
    margin-top: 10px;
  }
  .context{
    width: 250px;
    height: 50px;
    font-size: 14px;
    position: relative;
    margin-top: 20px;
    left: 22px;
    child-align: left;
    transition: 0.5s;
  }
  .subContext{
    display: block;
    margin-bottom: 10px;
    width: 250px;
    text-align: left;
  }
</style>
