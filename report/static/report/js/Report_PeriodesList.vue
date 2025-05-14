<template>
    <div style="margin: 50px;">
        <div>
            <b-row>
                <h2>Bulletin: Périodes</h2>
            </b-row>

            <b-row>
                <b-col
                    cols="12"
                    sm="3"
                >
                    <b-button
                        variant="success"
                        to="/period_form/"
                    >
                        Ajouter +
                    </b-button>
                </b-col>
            </b-row>
            <b-row
                class="card px-4 mt-2"
                v-for="period in periodEntries"
                :key="period.id"
            >
                <b-col>
                    <h5>
                        Période {{ period.periodNum }} ({{ scholarYears[period.scholarYear] }})                        
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
// import { BLink } from "bootstrap-vue-next";
import Moment from "moment";
import "moment/dist/locale/fr";
Moment.locale("fr");

export default{
    data: function(){
        return {
            periodEntries : [],
            periodEntriesCount: 0,
            scholarYears : [],
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
                    response.data.results.map(item => {
                        this.scholarYears[item.id] = item.label;
                        item[item.id] = item.label;
                        //item.value = item.label;
                        delete item.id;
                        delete item.label;
                        delete item.dateEnd;
                        delete item.dateStart;
                    });
                    console.log(this.scholarYears);
                });
        },
        findScholarYear: function(id){
            return this.scholarYears.find(id);
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
