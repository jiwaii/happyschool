<template>
    <div style="margin: 50px;">
        <div>
            <b-row>
                <h2>Bulletin: Nouvelle Periode</h2>
            </b-row>
            <b-row>
                <b-form
                    @submit="submit"
                    @reset="reset"
                >
                    <b-card style="width: 700px;">
                        <b-row>
                            <b-col>
                                <b-form-group
                                    label="Commence le"
                                    label-for="input-dateStart"
                                >
                                    <b-form-datepicker
                                        id="input-dateStart"
                                        type="text"
                                        v-model="form.dateStart"
                                    />
                                </b-form-group>
                            </b-col>
                            <b-col>
                                <b-form-group
                                    label="Termine le"
                                    label-for="input-dateEnd"
                                >
                                    <b-form-datepicker
                                        id="input-dateEnd"
                                        type="text"
                                        :min="form.dateStart"
                                        v-model="form.dateEnd"
                                    />
                                </b-form-group>
                                <b-form-group
                                    label="Numero de période"
                                    label-for="input-periodNum"
                                >
                                    <b-form-input
                                        id="input-periodNum"
                                        type="number"
                                        min="1"
                                        max="10"
                                        v-model="form.periodNum"
                                    />
                                    <b-form-invalid-feedback id="input-periodNum-feedback">
                                        Existe déjà !
                                    </b-form-invalid-feedback>
                                </b-form-group>
                            </b-col>
                            <b-col>
                                <b-form-group
                                    label="Année scolaire"
                                    label-for="input-scholarYear"
                                >
                                    <b-form-select
                                        id="input-scholarYear"
                                        v-model="form.scholarYear"
                                        :options="scholaryearOptions"
                                        value-field="id"
                                        text-field="label"
                                    />
                                </b-form-group>
                            </b-col>
                        </b-row>
                        <b-container class="bv-example-row">
                            <b-row>
                                <b-col>
                                    <b-button
                                        @click="submit"
                                        variant="primary"
                                        :disabled="sending"
                                    >
                                        {{ (this.id > 0) ? "Mettre à jour":"Soumettre" }}
                                    </b-button>
                                </b-col>
                                <b-col style="text-align:right ;">
                                    <b-button
                                        @click="deleteItem"
                                        v-if="this.id > 0"
                                        variant="danger"
                                        :disabled="sending"
                                    >
                                        Supprimer
                                    </b-button>
                                </b-col>
                            </b-row>
                        </b-container>
                    </b-card>
                </b-form>
            </b-row>
        </div>
    </div>
</template>

<script>


// import { options } from "@fullcalendar/core/preact.js";
import axios from "axios";
import Moment from "moment";
import "moment/dist/locale/fr";
Moment.locale("fr");

const token = { xsrfCookieName: "csrftoken", xsrfHeaderName: "X-CSRFToken" };

export default {
    props:{
        id:{
            type: String,
            default: "0",
        }
    },
    data: function () {
        return {
            form: {
                periodNum: "",
                dateStart: "",
                dateEnd: "",
                scholarYear:""
            },
            noExist: null,
            scholaryearOptions:[]
        };
    },
    methods: {
        convertDateFr: function (date) {
            return Moment(date).calendar();
        },
        submit: function () {
            if(this.id != "0"){
                axios.put(`api/period/${this.id}/`,this.form,token);
                this.$router.push("/periods/");
            }else{
                axios.post("api/period/",this.form,token);
                this.$router.push("/periods/");
            }
            console.log("submit period");
        },
        deleteItem : function(){
            console.log("delete id : "+this.id);
            axios.delete(`api/period/${this.id}/`,token);
            this.$router.push("/periods/");
        },
         
        loadItem(){
            axios.get(`api/period/${this.id}/`,token)
                .then(response =>{
                    if(response.data){
                        this.form.periodNum = response.data.periodNum;
                        this.form.dateStart = response.data.dateStart;
                        this.form.dateEnd = response.data.dateEnd;
                        this.form.scholarYear = response.data.scholarYear.id;
                    }
                });
        },
        loadScholaryearOptions(){
            axios.get("api/scholaryear_exist/",token)
                .then(response =>{
                    if(response.data){
                        this.scholaryearOptions = response.data.results;
                    }});
        },
        delete: function(){
            //
        }
    },
    mounted: function () {
        if(this.id != "0") this.loadItem();
        this.loadScholaryearOptions();
    }
};
</script>
