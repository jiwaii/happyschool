<template>
    <div style="margin: 50px;">
        <div>
            <b-row>
                <h2>Bulletin: Périodes</h2>
            </b-row>

            <BRow>
                <BCol
                    cols="6"
                    sm="2"
                >
                    <b-button
                        variant="success"
                        to="/period_form/"
                    >
                        Ajouter +
                    </b-button>
                </BCol>
               
                <BCol cols="3">
                    <BFormSelect
                        v-model="scholarYearsSelected"
                        :options="scholarYearsOptions"
                        value-field="id"
                        text-field="name"
                        size="lg"
                        class="mb-3"
                        @change="search"
                    >
                        <template #first>
                            <BFormSelectOption
                                :value="null"
                                disabled
                            >
                                Choisir l'année scolaire
                            </BFormSelectOption>
                        </template>
                    </BFormSelect>
                </BCol>
                <BCol cols="2">
                    <b-form-input
                        placeholder="# période"
                        @keyup.enter="this.search"
                        id="input-scholarYearlabel"
                        type="number"
                        size="lg"
                        v-model="keyword"
                    />
                </BCol>
            </BRow>
            <b-row
                class="card px-4 mt-2"
                v-for="period in periodEntries"
                :key="period.id"
            >
                <b-col>
                    <h5>
                        Période 
                        <BBadge>
                            {{ period.periodNum }}
                        </BBadge> ({{ scholarYears[period.scholarYear] }})                        
                        <!-- ({{ scholarYears.find((scholarYear) => scholarYear.id === period.scholarYear).value }}) -->
                    </h5>
                </b-col>
                <b-col>
                    {{ convertDateFr(period.dateStart) }} au {{ convertDateFr(period.dateEnd) }}
                </b-col>

                <b-col style="text-align: right;">
                    <div class="text-right">
                        <BLink
                            variant="outline-primary"
                            size="sm"
                            :to="'/period_edit/' + period.id + '/'"
                            class="card-link"
                        >
                            Modifier
                        </BLink>
                    </div>
                    <!-- <a
                        :href="`#/`"
                        @click="editScholaryear"
                        class="card-link"
                    ><b-icon
                        icon="pencil-square"
                        variant="success"
                    /></a> -->
                </b-col>
            </b-row>
        </div>
    </div>
</template>
<script>

import axios from "axios";
//import { BCol } from "bootstrap-vue-next";
// import { BLink } from "bootstrap-vue-next";
import Moment from "moment";
import "moment/dist/locale/fr";
import {ref} from "vue";
Moment.locale("fr");

export default{
    data: function(){
        return {
            periodEntries : [],
            periodEntriesCount: 0,
            scholarYears : [],
            scholarYearsOptions : [],
            scholarYearsSelected: ref(null),
            keyword : "",
            search : () => {
                console.log(this.keyword);
                this.findEntries();
            },
        };
    },
    methods:{
        loadEntries: function(){
            return axios.get("api/period/")
                .then(response =>{
                    this.periodEntries = response.data.results;
                    this.periodEntriesCount = response.data.count;
                    this.loaded = true;
                    console.log("periods :");
                    console.log(this.periodEntries);
                });
        },
        loadScolaryears: function(){
            return axios.get("api/scholaryear_exist")
                .then(response =>{
                    this.scholarYearsOptions = response.data.results;
                    response.data.results.map(item => {
                        this.scholarYears[item.id] = item.label;
                        //item[item.id] = item.label;
                        //item.value = item.label;
                        // delete item.id;
                        
                        item.name = item.label; 
                        delete item.label;
                        delete item.dateEnd;
                        delete item.dateStart;
                    });
                    
                    console.log(this.scholarYearsOptions);
                });
        },
        findEntries: function(){
            return axios.get(`api/period/?periodNum=${this.keyword}&scholarYear__id=${this.scholarYearsSelected}`)
                .then(response =>{
                    this.periodEntries = response.data.results;
                    this.periodEntriesCount = response.data.count;
                    this.loaded = true;
                    console.log("periods :");
                    console.log(this.periodEntries);
                });
        },
        convertDateFr: function(date){
            return Moment(date).calendar();
        }
    },
    mounted:function(){
        this.loadEntries();
        this.loadScolaryears();
        
        
    }
};
</script>
