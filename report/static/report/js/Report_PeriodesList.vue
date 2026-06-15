<template>
    <!-- <BToast
        v-model="showToast"
        variant="info"
        solid
    >
        <template #title> Mon Toast</template>
        {{ scholarYears[scholarYearsSelected]}} As tu vu mon toast ?
    </BToast> -->
    <div style="margin: 50px;">
        <div>
            <b-row>
                <h2>Bulletin: Périodes</h2>
            </b-row>

            <BRow>
                <BCol
                    cols="6"
                    sm="2"
                >
                    <b-button
                        variant="success"
                        to="/period_form/"
                    >
                        Ajouter +
                    </b-button>
                </BCol>

                <BCol cols="3">
                    <BFormSelect
                        v-model="scholarYearsSelected"
                        :options="scholarYearsOptions"
                        value-field="id"
                        text-field="name"
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
                <BCol cols="2">
                    <b-form-input
                        placeholder="Période"
                        @change="this.search"
                        id="input-scholarYearlabel"
                        type="number"
                        size="lg"
                        v-model="keyword"
                        min="1"
                        max="9"
                    />
                </BCol>
            </BRow>
            <b-row
                class="card px-4 mt-2"
                v-for="period in periodEntries"
                :key="period.id"
            >
                <b-col>
                    <h5>
                        Période
                        <BBadge>
                            {{ period.periodNum }}
                        </BBadge>
                        ({{ scholarYears[period.scholarYear] }}) {{ period.classeGroupLabel }}
                        <!-- {{ classeGroups[period.classeGroup] }}                       -->
                        <!-- ({{ scholarYears.find((scholarYear) => scholarYear.id === period.scholarYear).value }}) -->
                    </h5>
                </b-col>
                <b-col>
                    {{ convertDateFr(period.dateStart) }} au {{ convertDateFr(period.dateEnd) }}
                </b-col>

                <b-col style="text-align: right;">
                    <div class="text-right">
                        <b-link
                            variant="outline-primary"
                            size="sm"
                            :to="'/period_edit/' + period.id + '/'"
                            class="card-link"
                        >
                            Modifier
                        </b-link>
                    </div>
                    <!-- <a
                        :href="`#/`"
                        @click="editScholaryear"
                        class="card-link"
                    ><b-icon
                        icon="pencil-square"
                        variant="success"
                    /></a> -->
                </b-col>
            </b-row>
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
            classeGroups: [],
            keyword: "",
            search: () => {
                console.log(this.keyword);
                this.findEntries();
            },
            // showToast : false,
        };
    },
    methods: {
        loadEntries: function () {
            return axios.get("api/period/")
                .then((response) => {
                    this.periodEntries = response.data.results;
                    this.periodEntriesCount = response.data.count;
                    this.loaded = true;
                    console.log("periods :");
                    console.log(this.periodEntries);
                });
        },
        loadScolaryears: function () {
            return axios.get("api/scholaryear_exist")
                .then((response) => {
                    this.scholarYearsOptions = response.data.results;
                    response.data.results.map((item) => {
                        this.scholarYears[item.id] = item.label;
                        // item[item.id] = item.label;
                        // item.value = item.label;
                        // delete item.id;

                        item.name = item.label;
                        delete item.label;
                        delete item.dateEnd;
                        delete item.dateStart;
                    });
                    console.log(this.scholarYears);
                    console.log(this.scholarYearsOptions);
                });
        },
        loadClasseGroups: function () {
            return axios.get("api/classegroup")
                .then((response) => {
                    // this.classeGroup = response.data.results;
                    response.data.results.map((item) => {
                        this.classeGroups[item.id] = item.title;
                    });
                    console.log(this.classeGroups);
                });
        },
        findEntries: function () {
            // this.showToast = true;
            return axios.get(`api/period/?periodNum=${this.keyword}&scholarYear__id=${this.scholarYearsSelected}`)
                .then((response) => {
                    this.periodEntries = response.data.results;
                    this.periodEntriesCount = response.data.count;
                    this.loaded = true;
                    console.log("periods :");
                    console.log(this.periodEntries);
                });
        },
        convertDateFr: function (date) {
            // return Moment(date).calendar();
            return DateTime.fromISO(date).toLocaleString();
        },
    },
    mounted: function () {
        // this.loadEntries();
        this.loadScolaryears();
        this.loadClasseGroups();
    },
};
</script>
