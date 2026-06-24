<template>
    <BContainer>
        <h1>Mes cours donnés</h1>
        <BRow>
            <BCol
                id="nav-info"
                sm="2"
            >
                <div class="d-grid gap-2">
                    <BButton
                        :to="`/`"
                    >
                        Retour (Menu principale)
                    </BButton>
                </div>
            </BCol>
            <BCol id="table">
                <BTable
                    striped
                    hover
                    :items="entries"
                    :fields="btableFields"
                >
                    <template #cell(course)="data">
                        {{ data.value.short_name }} {{ data.value.long_name }}
                        <!-- {{ data.value.scolar_year }} -->
                    </template>
                    <template #cell(id)="id">
                        <BButton
                            size="sm"
                            class="me-1"
                            :to="'/cotation/'+id.value"
                        >
                            Voir cotations
                        </BButton>
                    </template>
                </BTable>
            </BCol>
        </BRow>
    </BContainer>
</template>

<script>

import axios from "axios";

export default {
    components: {

    },
    data: function () {
        return {
            btableFields: ["course", { key: "id", label: "Option" }],
            entries: [],
        };
    },
    methods: {
        getGivenCourses() {
            return axios.get("/core/api/given_course_info/")
                .then((response) => {
                    this.entries = response.data.results;
                });
        },
    },
    mounted: function () {
        this.getGivenCourses();
    },
};

</script>
