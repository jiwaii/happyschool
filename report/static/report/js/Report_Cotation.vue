<template>
    <BContainer>
        <h1>Mes cotations</h1>
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
            <BCol id="table">
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
                            :to="`/`"
                        >
                            Noter
                        </BButton>
                    </template>
                </BTable>
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
            entries: [],
            fields: [
                { key: "title", label: "Titre cot" },
                { key: "max_note", label: "Note maximale" },
                { key: "made_date", label: "En date du" },
                { key: "id", label: "Option" },
            ],
        };
    },
    methods: {
        getCotations() {
            return axios.get(`/report/api/cotation/?given_course=${this.givencours}`)
                .then((response) => {
                    this.entries = response.data.results;
                });
        },
        convertDateFr: function (date) {
            // return Moment(date).calendar();

            return DateTime.fromISO(date).toLocaleString();
        },
    },
    mounted: function () {
        this.getCotations();
    },
};

</script>
