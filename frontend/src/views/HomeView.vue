<template>
  <div v-if="$store.state.isAuthenticated" class="home">
      <TestBox 
        v-for="testcase in testcases"
        v-bind:key="testcase.id"
        v-bind:testcase="testcase" />
  </div>
  <div v-else class="home">
      <div class="column">Авторизируйтесь, чтобы проходить тестирование</div>
  </div>
</template>

<script>
import axios from 'axios'

import TestBox from '@/components/TestBox'

export default {
  name: 'Home',
  data() {
    return {
      testcases: []
    }
  },
  components: {
    TestBox
  },
  mounted() {
    this.getTestcases()

    document.title = 'Home'
  },
  methods: {
    async getTestcases() {
      this.$store.commit('setIsLoading', true)

      await axios
        .get('/api/v1/testcases/')
        .then(response => {
          this.testcases = response.data
        })
        .catch(error => {
          console.log(error)
        })

      this.$store.commit('setIsLoading', false)
    }
  }
}
</script>