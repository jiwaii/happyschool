<template>
    <BContainer>
        <h2 v-if="givenCoursInfo">
            Cotations
            {{ givenCoursInfo.course.short_name }}
            {{ givenCoursInfo.course.long_name }}
        </h2>
        <ul
            v-if="givenCoursInfo"
            style="display: inline-flex;list-style-type: none;"
        >
            <li
                v-for="teacher in givenCoursInfo.teachers"
                :key="teacher.id"
            >
                {{ teacher.fullname }} ,
            </li>
        </ul>
        <p>(devoirs, interrogations, examens)</p>

        <BRow>
            <BCol
                id="nav-info"
                sm="2"
            >
                <div class="d-grid gap-2">
                    <BButton
                        :to="`/givencourse/`"
                        rel="noopener"
                    >
                        Retour
                    </BButton>
                    <BButton
                        variant="success"
                        :to="`/cotation_form/${givencours}/${0}`"
                    >
                        Nouvelle cotation
                    </BButton>
                </div>
            </BCol>
            <BCol
                id="table"
                lg="7"
            >
                <BTable
                    striped
                    hover
                    :items="entries"
                    :fields="fields"
                >
                    <template #cell(made_date)="data">
                        {{ convertDateFr(data.value) }}
                    </template>
                    <template #cell(id)="id">
                        <BButton
                            size="sm"
                            variant="primary"
                            class="me-1"
                            :to="`/cotation_form/${givencours}/${id.value}`"
                        >
                            Details
                        </BButton>
                        <BButton
                            size="sm"
                            class="me-1"
                            variant="primary"
                            :to="`/cotation_notes/${id.value}`"
                        >
                            Voir (et évaluer)
                        </BButton>
                    </template>
                </BTable>
            </BCol>
            <BCol
                id="table-student-course"
            >
                <BTable
                    striped
                    hover
                    :items="entriesStudents"
                    :fields="fieldsStudents"
                >
                    <template #cell(full_name)="data">
                        {{ data.item.student_level.student.first_name }} {{ data.item.student_level.student.last_name }}
                        {{ data.item.student_level.classe.year }}{{ data.item.student_level.classe.letter.toUpperCase() }}
                    </template>
                </btable>
            </BCol>
        </BRow>
    </BContainer>
</template>

<script>

import axios from "axios";
import { DateTime } from "luxon";

export default {
    props: {
        givencours: {
            type: String,
            default: "0",
        },
    },
    data: function () {
        return {
            fullCoursTitle: "",
            givenCoursInfo: null,
            teachers: [],
            entries: [],
            entriesStudents: [],
            fields: [
                { key: "title", label: "Titre cot" },
                { key: "max_note", label: "Note maximale" },
                { key: "made_date", label: "En date du" },
                { key: "id", label: "" },
            ],
            fieldsStudents: [
                { key: "full_name", label: "Étudiant(e)s dans le cours" },
            ],
        };
    },
    methods: {
        getGivenCourseInfo() {
            return axios.get(`/core/api/given_course_info/${this.givencours}`)
                .then((response) => {
                    if (response.data) {
                        this.givenCoursInfo = response.data;
                        // let data = response.data;
                        // this.fullCoursTitle = `${data.course.short_name} ${data.display}`;
                        // this.teachers = data.teachers;
                    }
                });
        },
        getCotationsList() {
            return axios.get(`/report/api/cotation/?given_course=${this.givencours}`)
                .then((response) => {
                    if (response.data) {
                        this.entries = response.data.results;
                    }
                });
        },
        getStudentInCourse() {
            return axios.get(`/report/api/studentlevelcourse/?course=${this.givencours}`)
                .then((response) => {
                    if (response.data) {
                        this.entriesStudents = response.data.results;
                    }
                });
        },
        convertDateFr: function (date) {
            return DateTime.fromISO(date).toLocaleString();
        },
    },
    mounted: function () {
        this.getGivenCourseInfo();
        this.getCotationsList();
        this.getStudentInCourse();
    },
};

</script>
