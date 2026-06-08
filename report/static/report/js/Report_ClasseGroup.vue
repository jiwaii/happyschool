<template>
    <BContainer>

        <h1>Classes</h1>

        <b-row
        class="card px-4 mt-2" style="background-image:linear-gradient(135deg,#C5CBE5,#eaf3fc);"
        v-for="classeGroup in entries"
        >
        <div>
            <h3 style="position: relative;
                left: -30px;
                color: grey;
                font-weight: bolder;">{{ classeGroup.studyYear }}e - {{ classeGroup.title }}:</h3>
            <ClassePad
            v-for="classe in classeGroup.classes"
            :label="classe.classe+classe.letter" 
            :id="classe.id"
            />
        </div>
        </b-row>
    </BContainer>
</template>

<script>
import axios from 'axios';
import Moment from "moment";
import "moment/dist/locale/fr"
import ClassePad from './Report_ClassePad.vue';
import { str } from 'ajv';
Moment.locale("fr")

export default{
    components:{
        ClassePad
    },
    data: function(){
        return {
            entries : [],
            fields : [
            {key: 'title', label:'Titre'},
            {key: 'studyYear', label:'Année d\'étude'},
            ]
        }
    },
    methods:{
        loadEntries:function(){
            return axios.get("api/classegroup/").then(
            response => {
                this.entries = response.data.results;
            }
            )
        }
    },
    mounted:function() {
        this.loadEntries();
    }
}

</script>