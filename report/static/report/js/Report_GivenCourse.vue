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
                    <template #cell(full_label)="full_label">
                        {{ full_label.item.course.short_name }}
                        {{ full_label.item.course.long_name }} -
                        {{ full_label.item.group.toUpperCase() }}
                        ({{ full_label.item.scholar_year.label }})
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
            btableFields: [
                { key: "full_label", label: "Cours enseigné" },
                { key: "id", label: "" }],
            entries: [],
            userMatricule: null,
            studentCourseEntries: [],
        };
    },
    methods: {
        getGivenCourses() {
            return axios.get(`/report/api/coursesresponsible/${this.userMatricule}/`)
                .then((response) => {
                    this.entries = response.data.courses;
                    console.log(this.entries);
                });
        },
        getUserMatricule() {
            // eslint-disable-next-line no-undef
            if (user_properties && user_properties.matricule) this.userMatricule = user_properties.matricule;
        },
    },
    mounted: function () {
        this.getUserMatricule();
        this.getGivenCourses();
    },
};

</script>
