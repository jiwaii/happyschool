<template>
    <BContainer>
        <div style="margin: 50px;">
            <div>
                <b-row>
                    <h2>Bulletin: Années scolaires</h2>
                </b-row>

                <b-row>
                    <b-col
                        cols="12"
                        sm="3"
                    >
                        <b-button
                            variant="success"
                            to="/scholaryears_form/"
                        >
                            Ajouter +
                        </b-button>
                    </b-col>
                </b-row>
            
                <b-row
                    class="card px-4 mt-2"
                    v-for="scholaryear in scholaryearEntries"
                    :key="scholaryear.id"
                >
                    <b-col>
                        <h5>
                            {{ scholaryear.label }}
                        </h5>
                    </b-col>
                    <b-col>
                        {{ convertDateFr(scholaryear.dateStart) }} au {{ convertDateFr(scholaryear.dateEnd) }}
                    </b-col>
                    <b-col style="text-align: right;">
                        <div class="text-right">
                            <BLink
                                variant="outline-primary"
                                size="sm"
                                :to="'/scholaryears_edit/' + scholaryear.id + '/'"
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
    </BContainer>
</template>
<script>

import axios from "axios";
// import { BContainer, BLink } from "bootstrap-vue-next";
import Moment from "moment";
import "moment/dist/locale/fr";
Moment.locale("fr");

export default{
    data: function(){
        return {
            scholaryearEntries : [],
            scholaryearEntriesCount: 0,
        };
    },
    methods:{
        loadEntries: function(){
            axios.get("/report/scholaryear/")
                .then(response =>{
                    console.log(response);
                    this.scholaryearEntries = response.data;
                    this.scholaryearEntriesCount = response.data.lenght;
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
