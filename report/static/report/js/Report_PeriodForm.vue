<template>
    <div style="margin: 50px;">
        <div>
            <b-row>
                <h2>Bulletin: {{ (this.id > 0) ? "Modifier":"Nouvelle" }} Periode</h2>
            </b-row>

            <b-row>
                <b-form
                    @submit="submit"
                    @reset="reset"
                >
                    <b-card style="width: 700px;">
                        <b-row style="padding: 15px;">
                            <b-col>
                                <b-form-group
                                    label="Commence le"
                                    label-for="input-dateStart"
                                >
                                    <BFormInput
                                        id="input-dateStart"
                                        type="date"
                                        v-model="form.dateStart"
                                    />
                                </b-form-group>
                                <b-form-group
                                    label="Année d'étude"
                                    label-for="input-classGroup"
                                >
                                <BFormSelect
                                        v-model="form.classeGroup"
                                        :options="classeGroupOptions"
                                        value-field="id"
                                        text-field="title"
                                    >
                                        <template #first>
                                            <option
                                                :value="null"
                                                disabled
                                            >
                                                Choisissez l'année d'étude
                                            </option>
                                        </template>
                                </BFormSelect>
                                </b-form-group>
                            </b-col>
                            <b-col>
                                <b-form-group
                                    label="Termine le"
                                    label-for="input-dateEnd"
                                >
                                    <BFormInput
                                        id="input-dateEnd"
                                        type="date"
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
                                    <BFormSelect
                                        v-model="form.scholarYear"
                                        :options="scholaryearOptions"
                                        value-field="id"
                                        text-field="labelYear"
                                    >
                                        <template #first>
                                            <option
                                                :value="null"
                                                disabled
                                            >
                                                Choisissez l'année
                                            </option>
                                        </template>
                                    </BFormSelect>
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
// import { BRow } from "bootstrap-vue-next";
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
                scholarYear:"",
                classeGroup:"",
            },
            noExist: null,
            scholaryearOptions:[],
            classeGroupOptions:[],
        };
    },
    methods: {
        convertDateFr: function (date) {
            return Moment(date).calendar();
        },
        submit: function () {
            console.log("submit period :");
            if(this.checkPeriodeAndScholaryear()){            
                if(this.id != "0"){
                    axios.put(`api/period/${this.id}/`,this.form,token).then(
                        () => {
                            this.$router.push("/periods/");
                        }).catch(
                        (error) =>{
                            console.log(error);
                        });
                
                }else{
                    axios.post("api/period/",this.form,token);
                    this.$router.push("/periods/");
                }
            }
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
                        this.form.scholarYear = response.data.scholarYear;
                        this.form.classeGroup = response.data.classeGroup;
                    }
                });
        },
        loadScholaryearOptions(){
            axios.get("api/scholaryear_exist/",token)
                .then(response =>{
                    if(response.data){
                        this.scholaryearOptions = response.data.results;
                        console.log(this.scholaryearOptions);

                        let myMap = this.scholaryearOptions.map(item => {
                            item.labelYear = item.label;
                            delete item.label;
                            return item;
                        });
                        console.log(myMap);
                    }});
        },
        loadClasseGroupOptions(){
            axios.get("api/classegroup/",token)
                .then(response => {
                    if(response.data){
                        this.classeGroupOptions = response.data.results;
                        console.log(this.classeGroupOptions)
                    }
                })
        },
        checkPeriodeAndScholaryear: function(){
            var scholarYearSelected = this.scholaryearOptions.find((scholarYear) => scholarYear.id === this.form.scholarYear);
            console.log(scholarYearSelected.dateEnd);
            if (this.form.dateStart < scholarYearSelected.dateStart){
                alert("Date de DÉBUT de période ("+this.form.dateStart+") est inférieur à la date d'entrés scolaire "+scholarYearSelected.dateStart);
                return false;
            } else if(this.form.dateEnd > scholarYearSelected.dateEnd){
                alert("Date de FIN de période ("+this.form.dateEnd+") est supérieur à la date de sortie scolaire "+scholarYearSelected.dateEnd);
                return false;
            } else{
                return true;
            }
            // VOIR ENCHEVAUCHEMENT ENTRE PERIODE AUSSI
        },
    },
    mounted: function () {
        if(this.id != "0") this.loadItem();
        this.loadScholaryearOptions();
        this.loadClasseGroupOptions();
    }
};
</script>
