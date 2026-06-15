<template>
    <BContainer>
        <div style="margin: 50px;">
            <div>
                <b-row>
                    <h2>Etudiants</h2>
                </b-row>
                <b-row>
                    <b-col
                        cols="12"
                        sm="3"
                    >
                        <b-button
                            variant="success"
                            to="/"
                        >
                            Ajouter +
                        </b-button>
                    </b-col>
                </b-row>
                <b-row>
                    <BTable
                        striped
                        hover
                        :fields="fields"
                        :items="entries"
                    >
                        <template #cell(student)="data">
                            {{ data.item.student.first_name }} {{ data.item.student.last_name }}
                        </template>
                    </BTable>
                </b-row>
            </div>
        </div>
    </BContainer>
</template>
<script>

import axios from "axios";
import { DateTime } from "luxon";

export default {
    data: function () {
        return {
            entries: [],
            entriesCount: 0,
            fields: [{ key: "student", label: "Étudiant" }, "classe", { key: "scholarYear", label: "Année scolaire" }],
        };
    },
    methods: {
        loadEntries: function () {
            axios.get("/report/api/studentlevel/")
                .then((response) => {
                    console.log(response);
                    this.entries = response.data.results;
                    this.entriesCount = response.data.results.lenght;
                    this.loaded = true;
                });
        },
        convertDateFr: function (date) {
            // return Moment(date).calendar();
            return DateTime.fromISO(date).toLocaleString();
        },
    },
    mounted: function () {
        this.loadEntries();
    },
};
</script>
