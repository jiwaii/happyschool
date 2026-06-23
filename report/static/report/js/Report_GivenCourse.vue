<template>
    <BContainer>
        <h1>Mes cours donnés</h1>
        <div>
            <BTable
            striped
            hover
            :items="entries"
            :fields="btableFields"
            >
            <template #cell(course)="data">
                {{ data.value.short_name}} {{ data.value.long_name}} 
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
</div>

</BContainer>
</template>

<script>

import axios from "axios";

export default {
    components: {
        
    },
    data: function () {
        return {
            btableFields: ['course',{key:'id',label:'Option'}],
            entries: [],
        };
    },
    methods: {
        getGivenCourses() {
            return axios.get('/core/api/given_course_info/')
            .then((response) => {
                this.entries = response.data.results
            })
        }
    },
    mounted: function () {
        this.getGivenCourses()
    },
};

</script>
