<template>
    <div style="margin: 50px;">
        <div>
            <BRow>
                <h2>Bulletin: {{ (this.id > 0) ? "Modifier":"Nouvelle" }} Periode</h2>
            </BRow>

            <BRow>
                <b-form
                    @submit="submit"
                    @reset="reset"
                >
                    <BCard style="width: 700px;">
                        <BRow style="padding: 15px;">
                            <BCol>
                                <b-form-group
                                    label="Commence le"
                                    label-for="input-dateStart"
                                >
                                    <BFormInput
                                        id="input-dateStart"
                                        type="date"
                                        v-model="form.date_start"
                                    />
                                </b-form-group>
                                <b-form-group
                                    label="Année d'étude"
                                    label-for="input-classGroup"
                                >
                                    <BFormSelect
                                        v-model="form.classe_group"
                                        :options="classeGroupOptions"
                                        value-field="id"
                                        text-field="label"
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
                            </BCol>
                            <BCol>
                                <b-form-group
                                    label="Termine le"
                                    label-for="input-dateEnd"
                                >
                                    <BFormInput
                                        id="input-dateEnd"
                                        type="date"
                                        :min="form.date_start"
                                        v-model="form.date_end"
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
                                        v-model="form.period_num"
                                    />
                                    <b-form-invalid-feedback id="input-periodNum-feedback">
                                        Existe déjà !
                                    </b-form-invalid-feedback>
                                </b-form-group>
                            </BCol>
                            <BCol>
                                <b-form-group
                                    label="Année scolaire"
                                    label-for="input-scholarYear"
                                >
                                    <BFormSelect
                                        v-model="form.scholar_year"
                                        :options="scholarYearOptions"
                                        value-field="id"
                                        text-field="label"
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
                            </BCol>
                        </BRow>
                        <BContainer class="bv-example-row">
                            <BRow>
                                <BCol>
                                    <BButton
                                        @click="submit"
                                        variant="primary"
                                        :disabled="sending"
                                    >
                                        {{ (this.id > 0) ? "Mettre à jour":"Soumettre" }}
                                    </BButton>
                                </BCol>
                                <BCol style="text-align:right ;">
                                    <BButton
                                        @click="deleteItem"
                                        v-if="this.id > 0"
                                        variant="danger"
                                        :disabled="sending"
                                    >
                                        Supprimer
                                    </BButton>
                                </BCol>
                            </BRow>
                        </BContainer>
                    </BCard>
                </b-form>
            </BRow>
        </div>
    </div>
</template>

<script>

import axios from "axios";
import { DateTime } from "luxon";

const token = { xsrfCookieName: "csrftoken", xsrfHeaderName: "X-CSRFToken" };

export default {
    props: {
        id: {
            type: String,
            default: "0",
        },
    },
    data: function () {
        return {
            form: {
                period_num: null,
                date_start: null,
                date_end: null,
                scholar_year: null,
                classe_group: null,
            },
            noExist: null,
            scholarYearOptions: [],
            classeGroupOptions: [],
        };
    },
    methods: {
        convertDateFr: function (date) {
            // return Moment(date).calendar();
            return DateTime.fromISO(date).toLocaleString();
        },
        submit: function () {
            if (this.checkPeriodeAndScholarYear()) {
                if (this.id != "0") {
                    axios.put(`/report/api/period/${this.id}/`, this.form, token).then(
                        () => {
                            this.$router.push("/periods/");
                        }).catch(
                        (error) => {
                            console.log(error);
                        });
                } else {
                    console.log("post");
                    axios.post("/report/api/period/", this.form, token).then((response) => {
                        this.$router.push("/periods/");
                    })
                        .catch((error) => {
                            // console.error("error GRR "+error);
                            console.log(error.response.data);
                            alert(error.response.data.non_field_errors);
                        })
                        .finally(() => {
                            console.log("Request completed");
                        });
                }
            }
        },
        deleteItem: function () {
            console.log("delete id : " + this.id);
            axios.delete(`/report/api/period/${this.id}/`, token);
            this.$router.push("/periods/");
        },

        loadItem() {
            axios.get(`/report/api/period/${this.id}/`, token)
                .then((response) => {
                    if (response.data) {
                        this.form = response.data;
                    }
                });
        },
        loadScholarYearOptions() {
            axios.get("/core/api/scholar_year/")
                .then((response) => {
                    if (response.data) {
                        this.scholarYearOptions = response.data.results;
                    }
                });
        },
        loadClasseGroupOptions() {
            axios.get("/core/api/classe_group/", token)
                .then((response) => {
                    if (response.data) {
                        this.classeGroupOptions = response.data.results;
                    }
                });
        },
        checkPeriodeAndScholarYear: function () {
            const scholarYearSelected = this.scholarYearOptions.find(scholarYear => scholarYear.id === this.form.scholar_year);
            console.log(scholarYearSelected.date_end);
            if (this.form.date_start < scholarYearSelected.date_start) {
                alert("Date de DÉBUT de période (" + this.form.date_start + ") est inférieur à la date de la rentrés scolaire " + scholarYearSelected.date_start);
                return false;
            } else if (this.form.date_end > scholarYearSelected.date_end) {
                alert("Date de FIN de période (" + this.form.date_end + ") est supérieur à la date de la sortie scolaire " + scholarYearSelected.date_end);
                return false;
            } else {
                return true;
            }
            // VOIR ENCHEVAUCHEMENT ENTRE PERIODE AUSSI
        },
    },
    mounted: function () {
        if (this.id != "0") this.loadItem();
        this.loadScholarYearOptions();
        this.loadClasseGroupOptions();
    },
};
</script>
