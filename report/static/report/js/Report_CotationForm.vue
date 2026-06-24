<template>
    <BContainer>
        <h1>{{ (this.id > 0) ? "Mettre à jour une":"Nouvelle" }} cotation </h1>
        <BRow>
            <BCol
                id="nav-info"
                sm="2"
            >
                <div class="d-grid gap-2">
                    <BButton
                        :to="`/cotation/${givencours}`"
                        rel="noopener"
                    >
                        Retour
                    </BButton>
                </div>
            </BCol>
            <BCol
                id="form"
                md="auto"
            >
                <BForm>
                    <BFormGroup
                        id="input-group-1"
                        label="Titre ou nom"
                        label-for="input-title"
                        description="Le titre ou le nom de votre cotation"
                    >
                        <BFormInput
                            id="input-title"
                            v-model="form.title"
                            placeholder="Titre de votre cotation"
                            required
                        />
                    </BFormGroup>
                    <BFormGroup
                        id="input-group-2"
                        label="Note maximale"
                        label-for="input-max_note"
                        description="Points maximale de votre cotation"
                    >
                        <BFormInput
                            id="input-max_note"
                            v-model="form.max_note"
                            type="number"
                            max="100"
                            min="1"
                            placeholder="Note maximale"
                            required
                        />
                    </BFormGroup>
                    <BFormGroup
                        id="input-group-3"
                        label="Date"
                        label-for="input-date"
                        description="Date de la cotation à remettre"
                    >
                        <BFormInput
                            id="input-date"
                            v-model="form.made_date"
                            type="date"
                            required
                        />
                    </BFormGroup>
                    <BButton
                        @click="submit(false)"
                        variant="primary"
                        :disabled="sending"
                    >
                        Soumettre
                    </BButton>
                    <BButton
                        @click="submit(true)"
                        variant="primary"
                        :disabled="sending"
                    >
                        Soumettre et évaluer
                    </BButton>
                    <BButton
                        v-if="(this.id > 0)"
                        @click="deleteItem"
                        variant="danger"
                        :disabled="sending"
                    >
                        Supprimer
                    </BButton>
                </BForm>
            </BCol>
        </BRow>
    </BContainer>
</template>

<script>

import axios from "axios";
import { DateTime } from "luxon";

const token = { xsrfCookieName: "csrftoken", xsrfHeaderName: "X-CSRFToken" };

export default {
    props: {
        givencours: {
            type: String,
            default: "0",
        },
        id: {
            type: String,
            default: "0",
        },
    },
    data: function () {
        return {
            form: {
                title: null,
                max_note: null,
                made_date: null,
                given_course: this.givencours,
            },
        };
    },
    methods: {
        getCotations() {
            return axios.get(`/report/api/cotation/?given_course=${this.givencours}`)
                .then((response) => {
                    this.entries = response.data.results;
                });
        },
        loadItem() {
            axios.get(`/report/api/cotation/${this.id}/`)
                .then((response) => {
                    if (response.data) {
                        this.form = response.data;
                    }
                });
        },
        convertDateFr: function (date) {
            // return Moment(date).calendar();

            return DateTime.fromISO(date).toLocaleString();
        },
        submit(evalRedirect) {
            // TODO : make note for redirection
            let url = (evalRedirect == true) ? "/" : `/cotation/${this.givencours}`;
            if (this.id != "0") {
                axios.put(`/report/api/cotation/${this.id}/`, this.form, token).then(
                    () => {
                        this.$router.push(url);
                    }).catch(
                    (error) => {
                        console.log(error);
                    });
            } else {
                console.log("post");
                axios.post("/report/api/cotation/", this.form, token).then(() => {
                    this.$router.push(url);
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
        },
        deleteItem() {
            console.log("delete");
        },
    },
    mounted: function () {
        if (this.id != "0") this.loadItem();
        this.getCotations();
    },
};

</script>
