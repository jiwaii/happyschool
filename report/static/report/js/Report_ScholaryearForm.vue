<template>
    <div style="margin: 50px;">
        <div>
            <b-row>
                <h2>Bulletin: {{(this.id > 0) ? "Editer" : "Nouvelle" }} années scolaires</h2>
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
                                    <BFormInput
                                        @update:model-value="genLabelStart"
                                        id="input-dateStart"
                                        type="date"
                                        v-model="form.dateStart"
                                    />
                                </b-form-group>
                            </b-col>
                            <b-col>
                                <b-form-group
                                    label="Termine le"
                                    label-for="input-dateEnd"
                                >
                                    <BFormInput
                                        @update:model-value="genLabelEnd"
                                        id="input-dateEnd"
                                        type="date"
                                        :min="form.dateStart"
                                        v-model="form.dateEnd"
                                    />
                                </b-form-group>
                                <b-form-group
                                    label="Titre année scolaire (généré)"
                                    label-for="input-label"
                                >
                                    <b-form-input
                                        readonly
                                        id="input-label"
                                        type="text"
                                        :state="noExist"
                                        v-model="form.label"
                                    />
                                    <b-form-invalid-feedback id="input-label-feedback">
                                        Existe déjà !
                                    </b-form-invalid-feedback>
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


import axios from "axios";
// import { BForm } from "bootstrap-vue-next";
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
                label: "",
                dateStart: "",
                dateEnd: "",
            },
            noExist: null

        };
    },
    methods: {
        convertDateFr: function (date) {
            return Moment(date).calendar();
        },
        submit: function () {
            console.log("Title : " + this.form.label +
                " \n Start : " + this.form.dateStart +
                " \n End : " + this.form.dateEnd);

            console.log("is Date ? : " + Moment.isDate(this.form.dateEnd));
            const token = { xsrfCookieName: "csrftoken", xsrfHeaderName: "X-CSRFToken" };
            if(this.id != "0"){
                axios.put(`api/scholaryear_exist/${this.id}/`,this.form,token);
                this.$router.push("/scholaryears/");
            }else{
                axios.get("api/scholaryear_exist/?label=" + this.form.label,
                    this.form, token)
                    .then((response) => {
                        console.log(response.data);
                        this.noExist = !response.data["count"] > 0;
                        if (this.noExist) {
                            console.log("axios post new scolaryear");
                            axios.post("/report/scholaryear/",
                                this.form, token)
                                .then((response) => {
                                    console.log("PASSED AXIOS : " + response);
                                    this.$router.push("/scholaryears/");
                                })
                                .catch(function (error) {
                                    console.log("ERROR AXIOS : ");
                                    console.log(error);
                                });
                        }
                    }).catch(function (error) {
                        console.log(error);
                    });
            }

        },
        deleteItem : function(){
            console.log("delete id : "+this.id);
            axios.delete(`scholaryear/${this.id}/`,token);
            this.$router.push("/scholaryears/");
        },
        genDateEnd: function (dateString) {
            let nextDate = new Date(dateString);
            nextDate.setDate(nextDate.getDate()+364);
            console.log("next date: "+nextDate);
            return nextDate.toLocaleDateString("en-ca");
        }
        ,
        genLabelStart: function (event) {
            console.log("Selected : "+event);
            if (this.form.label.indexOf("-") == 4) {
                let endYear = this.form.label.substring(5, 9);
                let startYear = event.split("-")[0];
                this.form.label = startYear + "-" + endYear;
                console.log("Title : "+this.form.label);
            } else {
                this.form.label = event.split("-")[0];
                this.form.dateEnd = this.genDateEnd(event);                
                this.form.label += "-" + this.form.dateEnd.split("-")[0];
            }
            
            console.log("dateEnd: "+this.form.dateEnd);
        },
        genLabelEnd: function (event) {
            if (this.form.label.indexOf("-") == 4) {
                let startYear = this.form.label.substring(0, 4);
                let endYear = event.split("-")[0];
                this.form.label = startYear + "-" + endYear;
            } else {
                this.form.label += "-" + event.split("-")[0];
            }
            console.log(event);
            console.log("dateEnd: "+this.form.dateEnd);
        },
        loadScholaryear(){
            axios.get(`scholaryear/${this.id}/`,token)
                .then(response =>{
                    if(response.data){
                        this.form.label = response.data.label;
                        this.form.dateStart = response.data.dateStart;
                        this.form.dateEnd = response.data.dateEnd;
                    }
                });
        },
        delete: function(){
            //
        }
    },
    mounted: function () {
        if(this.id != "0") this.loadScholaryear();
    }
};
</script>
