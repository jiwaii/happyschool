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
                        période {{ period.periodNum }} ({{ period.scholarYear.label }})  
                    </h5>
                </b-col>
                <b-col>
                    {{ convertDateFr(period.dateStart) }} au {{ convertDateFr(period.dateEnd) }}
                </b-col>

                <b-col style="text-align: right;">
                    <div class="text-right">
                        <b-btn
                            variant="outline-primary"
                            size="sm"
                            :to="'/period_edit/' + period.id + '/'"
                            class="card-link"
                        >
                            Modifier
                        </b-btn>
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
import Moment from "moment";
import "moment/dist/locale/fr";
Moment.locale("fr");

export default{
    data: function(){
        return {
            periodEntries : [],
            periodEntriesCount: 0,
        };
    },
    methods:{
        loadEntries: function(){
            axios.get("api/period/")
                .then(response =>{
                    console.log(response);
                    this.periodEntries = response.data.results;
                    this.periodEntriesCount = response.data.count;
                    this.loaded = true;
                });
        },
        convertDateFr: function(date){
            return Moment(date).calendar();
        }
    },
    mounted:function(){
        this.loadEntries();
    }
};
</script>
