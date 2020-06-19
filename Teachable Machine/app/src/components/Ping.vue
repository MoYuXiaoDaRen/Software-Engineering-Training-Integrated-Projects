<template>
  <div class="container">
    <button @click="getMessage">{{ msg }}</button>
    <button @click="postMessage">上传信息</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Ping',
  data () {
    return {
      msg: 'Hello!'
    }
  },
  methods: {
    getMessage () {
      const path = 'http://192.168.1.112:5000/ping'
      axios.get(path)
        .then((res) => {
          this.msg = res.data
        })
        .catch((error) => {
          console.error(error)
        })
    },
    postMessage () {
      const path = 'http://192.168.1.112:5000/message'
      axios.post(path, this.$qs.stringify({
        id: '123',
        name: 'gzx'
      }))
        .then((res) => {
          alert(res.data)
        })
        .catch((error) => {
          console.error(error)
        })
    }
  }
}
</script>
