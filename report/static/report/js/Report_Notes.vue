<template>
    <BContainer>
        <h2 v-if="cotationInfo">
            {{ cotationInfo.title }}
        </h2>
        <h3 v-if="cotationInfo">
            Sur {{ cotationInfo.max_note }} points
        </h3>
        <BRow>
            <BCol
                id="nav-info"
                sm="2"
            >
                <div class="d-grid gap-2">
                    <BButton
                        v-if="cotationInfo"
                        :to="`/cotation/${cotationInfo.given_course}`"
                    >
                        Retour
                    </BButton>
                    <BButton
                        @click="save()"
                        variant="success"
                    >
                        Soumettre
                    </BButton>
                </div>
            </BCol>
            <BCol
                v-if="entries"
            >
                <div
                    v-for="note in entries"
                    :key="note"
                >
                    <NoteRow :note="note" />
                </div>
            </BCol>
        </BRow>
    </BContainer>
</template>

<script>
import axios from "axios";
import NoteRow from "./Report_NotesRow.vue";

const token = { xsrfCookieName: "csrftoken", xsrfHeaderName: "X-CSRFToken" };

export default {
    props: {
        id: {
            type: String,
            default: "0",
        },
    },
    components: {
        NoteRow,

    },
    data: function () {
        return {
            entries: [],
            cotationInfo: null,
            form_note: {
                id: null,
                note: null,
                comment: null,
                cotation: null,
                student_level: null,
            },
        };
    },
    methods: {
        getNoteList() {
            return axios.get(`/report/api/note/?cotation=${this.id}`)
                .then((response) => {
                    if (response.data) {
                        this.entries = response.data.results;
                    }
                });
        },
        getCotationInfo() {
            return axios.get(`/report/api/cotation/${this.id}`)
                .then((response) => {
                    if (response.data) {
                        this.cotationInfo = response.data;
                    }
                });
        },
        save() {
            this.entries.forEach((note) => {
                // console.log(note);
                this.form_note.id = note.id;
                this.form_note.note = note.note;
                this.form_note.comment = note.comment;
                this.form_note.cotation = note.cotation;
                this.form_note.student_level = note.student_level;
                console.log(this.form_note);
                axios.put(`/report/api/note/${this.form_note.id}/`, this.form_note, token).then(
                    () => {
                        console.log(this.form_note);
                    },
                ).catch(
                    (error) => {
                        console.log(error);
                    },
                );
            });
        },
    },
    mounted: function () {
        this.getNoteList();
        this.getCotationInfo();
    },
};

</script>
