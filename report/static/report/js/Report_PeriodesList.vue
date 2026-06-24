<template>
    <div style="margin: 50px;">
        <div>
            <BRow>
                <h2>Bulletin: Périodes</h2>
            </BRow>

            <BRow>
                <BCol
                    cols="2"
                    sm="2"
                >
                    <BButton
                        variant="success"
                        to="/period_form/"
                    >
                        Ajouter +
                    </BButton>
                </BCol>

                <BCol cols="3">
                    <BFormSelect
                        v-model="scholarYearsSelected"
                        :options="scholarYearsOptions"
                        value-field="id"
                        text-field="label"
                        size="lg"
                        class="mb-3"
                        @change="search"
                    >
                        <template #first>
                            <BFormSelectOption
                                value=""
                                disabled
                            >
                                Année scolaire
                            </BFormSelectOption>
                        </template>
                    </BFormSelect>
                </BCol>

                <BCol cols="5">
                    <BFormSelect
                        v-model="classeGroupsSelected"
                        :options="classeGroupsOptions"
                        value-field="id"
                        text-field="label"
                        size="lg"
                        class="mb-3"
                        @change="search"
                    >
                        <template #first>
                            <BFormSelectOption
                                value=""
                                disabled
                            >
                                Classe
                            </BFormSelectOption>
                        </template>
                    </BFormSelect>
                </BCol>
            </BRow>
            <BRow
                v-if="scholarYearsOptions.length > 0 && classeGroupsOptions.length > 0"
            >
                <BCard
                    class="px-4 mt-2"
                    v-for="period in periodEntries"
                    :key="period.id"
                    no-body
                >
                    <BCol>
                        <h5>
                            Période
                            <BBadge>
                                {{ period.period_mabel }}
                            </BBadge>
                            ({{ scholarYearsOptions.find(sYO => sYO.id === period.scholar_year).label }})
                            {{ classeGroupsOptions.find(cG => cG.id === period.classe_group).label }}
                        <!-- {{ classeGroups[period.classeGroup] }}                       -->
                        <!-- ({{ scholarYears.find((scholarYear) => scholarYear.id === period.scholarYear).value }}) -->
                        </h5>
                    </BCol>
                    <BCol>
                        {{ convertDateFr(period.date_start) }} au {{ convertDateFr(period.date_end) }}
                    </BCol>

                    <BCol style="text-align: right;">
                        <div class="text-right">
                            <BLink
                                variant="outline-primary"
                                size="sm"
                                :to="'/period_edit/' + period.id + '/'"
                                class="card-link"
                            >
                                Modifier
                            </BLink>
                        </div>
                    <!-- <a
                        :href="`#/`"
                        @click="editScholaryear"
                        class="card-link"
                    ><b-icon
                        icon="pencil-square"
                        variant="success"
                    /></a> -->
                    </BCol>
                </BCard>
            </BRow>
        </div>
    </div>
</template>
<script>

import axios from "axios";
import { DateTime } from "luxon";

export default {
    data: function () {
        return {
            periodEntries: [],
            periodEntriesCount: 0,
            scholarYears: [],
            scholarYearsOptions: [],
            scholarYearsSelected: "",
            classeGroupsOptions: [],
            classeGroupsSelected: "",
            search: () => {
                console.log(this.keyword);
                this.findEntries();
            },
            // showToast : false,
        };
    },
    methods: {
        loadEntries: function () {
            return axios.get("/report/api/period/")
                .then((response) => {
                    this.periodEntries = response.data.results;
                    this.periodEntriesCount = response.data.count;
                    this.loaded = true;
                    console.log("periods :");
                    console.log(this.periodEntries);
                });
        },
        loadScolaryears: function () {
            return axios.get("/core/api/scholar_year/")
                .then((response) => {
                    this.scholarYearsOptions = response.data.results;
                });
        },
        loadClasseGroups: function () {
            return axios.get("/core/api/classe_group/")
                .then((response) => {
                    const teachingLabel = new Map([
                        [1, "Primaire"],
                        [2, "Secondaire"],
                        [3, "Maternel"],
                    ]);
                    this.classeGroupsOptions = response.data.results;
                    this.classeGroupsOptions = response.data.results.map((item) => {
                        item.label = item.label + " - " + teachingLabel.get(item.teaching);
                        return item;
                    });
                });
        },
        findEntries: function () {
            return axios.get(`/report/api/period/?classe_group=${this.classeGroupsSelected}&scholar_year__id=${this.scholarYearsSelected}`)

                .then((response) => {
                    this.periodEntries = response.data.results;
                    this.periodEntriesCount = response.data.count;
                    this.loaded = true;
                });
        },
        convertDateFr: function (date) {
            // return Moment(date).calendar();

            return DateTime.fromISO(date).toLocaleString();
        },
    },
    mounted: function () {
        // TODO Make a global promise in order to assign data variables in the correct order and simultanuesly.
        this.loadEntries();
        this.loadScolaryears();
        this.loadClasseGroups();
    },
};
</script>
