<template>
    <div class="page-testcase">
        <div class="columns is-multiline">
            <div class="column is-9">
                <div class="column"><h1 class="title">{{ testcase.title }}</h1></div>
                <div class="column" v-for="question in testcase.questions">
                    <div v-if="value==question.id">
                        <div><h2 class="subtitle">{{question.title}}</h2></div>
                        <div v-for="option in question.options">
                            <input class="checkbox" type="checkbox" :value="option.id" v-model="chosenOptions[question.id]">
                            {{option.text}}
                        </div>
                        <button class="button" v-on:click="nextQuestion" v-if="!done && chosenOptions[question.id].length != 0">Sled</button>
                        <button class="button" v-on:click="convert" v-if="done && chosenOptions[question.id].length != 0">Поприветствовать</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'TestCase',
    data() {
        return {
            testcase: {},
            chosenOptions: {},
            answers: [],
            value: 0,
            questionGenerator: [],
            done: false,
        }
    },
    mounted() {
        this.getTestcase() 
    },
    methods: {
        async getTestcase() {
            this.$store.commit('setIsLoading', true)

            const testcase_slug = this.$route.params.testcase_slug

            await axios
                .get(`/api/v1/testcases/${testcase_slug}`)
                .then(response => {
                    this.testcase = response.data
                    //this.chosenOptions = response.data.questions
                    response.data.questions.forEach((question) => {
                        this.chosenOptions[question.id] = []
                        this.questionGenerator.push(question.id)
                    })
                    this.value = this.questionGenerator.shift()
                    document.title = this.testcase.title + ' | Testcase'})
                .catch(error => {
                    console.log(error)
                })
            
            this.$store.commit('setIsLoading', false)
        },
        async convert() {
            for (const [key, value] of Object.entries(this.chosenOptions)){
                let options = []
                value.forEach((option) => {
                    options.push({"id": option})
                })
                this.answers.push({"question": {"id": key}, "options": options})
            }

            let data = {"test_case": this.testcase.id, "answers": this.answers}
            await axios
                .post(`/api/v1/completed/`, data)
                .then(response => {
                        this.$router.push(`/${this.testcase.slug}/result/`)
                    })
                .catch(error => {
                    console.log(error)
                })
        },
        nextQuestion(){
            this.value = this.questionGenerator.shift();
            if (this.questionGenerator.length == 0){
                this.done = true;
            }
        }
    }
}
</script>