<template>
    <BContainer>
        <h1>Mes cotations (devoir, interrogations, examens)</h1>
        <BButton variant="success">
            Nouvelle cotation
        </BButton>            
        
        <BTable
        striped
        hover
        :items="entries"
        :fields="fields"
        >
        <template #cell(made_date)="data">
            {{ convertDateFr(data.value) }}
        </template>
    </BTable>
    
</BContainer>
</template>

<script>

import axios from "axios";
import { DateTime } from "luxon";

export default {
    props: {
        givencours: {
            type: String,
            default: "0",
        },
    },
    data: function () {
        return {
            entries: [],
            fields:[
            {key:'title', label:'Titre cot'},
            {key:'max_note',label:'Note maximale'},
            {key:'made_date',label:'En date du'}
            ]
        };
    },
    methods: {
        getCotations() {
            return axios.get(`/report/api/cotation/?given_course=${this.givencours}`)
            .then((response) => {
                this.entries = response.data.results
            })
        },
        convertDateFr: function (date) {
            // return Moment(date).calendar();
            
            return DateTime.fromISO(date).toLocaleString();
        }       
    },
    mounted: function () {
        this.getCotations()
    },
};

</script>
