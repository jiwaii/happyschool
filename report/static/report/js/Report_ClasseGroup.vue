<template>
    <BContainer>
        <h1>Classes</h1>
        <BRow
            class="card px-4 mt-2"
            style="background-image:linear-gradient(135deg,#C5CBE5,#eaf3fc);"
            v-for="classeGroup in entries"
            :key="classeGroup.id"
        >
            <div>
                <h3
                    style="position: relative;
                left: -30px;
                color: grey;
                font-weight: bolder;"
                >
                    {{ classeGroup.studyYear }}e - {{ classeGroup.title }}:
                </h3>
                <ClassePad
                    v-for="classe in classeGroup.classes"
                    :key="classe.id"
                    :label="classe.classe+classe.letter"
                    :id="classe.id"
                />
            </div>
        </BRow>
    </BContainer>
</template>

<script>
import axios from "axios";

import ClassePad from "./Report_ClassePad.vue";

export default {
    components: {
        ClassePad,
    },
    data: function () {
        return {
            entries: [],
            fields: [
                { key: "title", label: "Titre" },
                { key: "studyYear", label: "Année d'étude" },
            ],
        };
    },
    methods: {
        loadEntries: function () {
            return axios.get("api/classegroup/").then(
                (response) => {
                    this.entries = response.data.results;
                },
            );
        },
    },
    mounted: function () {
        this.loadEntries();
    },
};

</script>
