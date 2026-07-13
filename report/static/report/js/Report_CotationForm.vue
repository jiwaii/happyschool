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
            studentsInCourse: [],
            form_note: {
                note: null,
                comment: null,
                cotation: null,
                student_level: null,
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
        getStudentInCourse() {
            return axios.get(`/report/api/studentlevelcourse/?course=${this.givencours}`)
                .then((response) => {
                    if (response.data) {
                        this.studentsInCourse = response.data.results;
                    }
                });
        },
        createNote(cotation_id, student_level_id) {
            this.form_note.note = 0;
            this.form_note.comment = "";
            this.form_note.cotation = cotation_id;
            this.form_note.student_level = student_level_id;
            axios.post("/report/api/note/", this.form_note, token).catch((err) => {
                console.log(err);
            });
        },
        convertDateFr: function (date) {
            // return Moment(date).calendar();

            return DateTime.fromISO(date).toLocaleString();
        },
        submit(evalRedirect) {
            let url = "";
            if (this.id != "0") {
                axios.put(`/report/api/cotation/${this.id}/`, this.form, token).then(
                    () => {
                        url = (evalRedirect == true) ? `/cotation_notes/${this.id}` : `/cotation/${this.givencours}`;
                        this.$router.push(url);
                    }).catch(
                    (error) => {
                        console.log(error);
                    });
            } else {
                axios.post("/report/api/cotation/", this.form, token).then((response) => {
                    let newCotation_id = response.data.id;
                    this.studentsInCourse.forEach(
                        (student) => {
                            this.createNote(newCotation_id, student.student_level.id);
                        },
                    );
                    let url = (evalRedirect == true) ? `/cotation_notes/${newCotation_id}` : `/cotation/${this.givencours}`;
                    this.$router.push(url);
                })
                    .catch((error) => {
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
            axios.delete(`/report/api/cotation/${this.id}/`, token).then(
                () => {
                    this.$router.push(`/cotation/${this.givencours}`);
                }).catch(
                (error) => {
                    console.log(error);
                });
        },
    },
    mounted: function () {
        if (this.id != "0") {
            // update cotation: load items only
            this.loadItem();
        } else {
            // new cotations : load Students to create notes
            this.getStudentInCourse();
        };
        this.getCotations();
    },
};

</script>
