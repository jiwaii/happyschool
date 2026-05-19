<template>
<h1>Classes par année d'étude</h1>
    <div>
    <!-- <BTable
      striped
      hover
      :items="this.entries"
      :fields="this.fields"
    /> -->
    </div>
    <b-row
    class="card px-4 mt-2" 
    v-for="classeGroup in entries"
    >
        <div>
			
            <h4>{{ classeGroup.studyYear }} ({{ classeGroup.title }}) :</h4>
            <ClassePad
            v-for="classe in classeGroup.classes"
            :label="classe"/>
        </div>
    </b-row>
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