<template>
    <div class="column is-3">
        <h3 class="is-size-4">{{ testcase.title }}</h3>
        <router-link v-if="!testcase.completed" v-bind:to="testcase.get_absolute_url" class="button is-dark mt-4">Пройти тест</router-link>
        <router-link v-else v-bind:to="testcase.get_absolute_url + 'result/'" class="button is-dark mt-4">Результат</router-link>
    </div>
</template>

<script>
export default {
    name: 'TestBox',
    props: {
        testcase: Object
    }
}
</script>

<style scoped>
  .image {
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
  }
</style>