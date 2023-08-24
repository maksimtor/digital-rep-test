<template>
    <div class="page-testcase">
        <div class="columns is-multiline">
            <div class="column is-9">
                <div class="column"><h1 class="title">Ваши результаты:</h1></div>
                <div class="column" v-for="answer in result.answers">
                    <h2 class="subtitle">{{answer.question.title}}</h2>
                    Ваш ответ: <div v-for="option in answer.options">{{option.text}}</div>
                    Правильный ответ: <span v-for="option in answer.question.options">
                        <div v-if="option.correct">{{option.text}}</div>
                        </span>
                </div>
                <div class="column">
                У вас {{result.right_answers}} правильных ответов и {{result.wrong_answers}} неправильных.<br>
                Результат: {{result.result}}%.
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'TestCaseResult',
    data() {
        return {
            result: {},
        }
    },
    mounted() {
        this.getResult() 
    },
    methods: {
        async getResult() {
            this.$store.commit('setIsLoading', true)

            const testcase_slug = this.$route.params.testcase_slug

            await axios
                .get(`/api/v1/testcases/${testcase_slug}/result/`)
                .then(response => {
                    this.result = response.data
                    })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        },
    }
}
</script>