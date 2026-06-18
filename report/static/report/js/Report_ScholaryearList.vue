<template>
    <BContainer>
        <div style="margin: 50px;">
            <div>
                <BRow>
                    <h2>Bulletin: Années scolaires</h2>
                </BRow>

                <BRow>
                    <BCol
                        cols="12"
                        sm="3"
                    >
                        <BButton
                            variant="success"
                            to="/scholaryears_form/"
                        >
                            Ajouter +
                        </BButton>
                    </BCol>
                </BRow>

                <BRow
                    class="card px-4 mt-2"
                    v-for="scholaryear in scholaryearEntries"
                    :key="scholaryear.id"
                >
                    <BCol>
                        <h5>
                            {{ scholaryear.label }}
                        </h5>
                    </BCol>
                    <BCol>
                        {{ convertDateFr(scholaryear.dateStart) }} au {{ convertDateFr(scholaryear.dateEnd) }}
                    </BCol>
                    <BCol style="text-align: right;">
                        <div class="text-right">
                            <BLink
                                variant="outline-primary"
                                size="sm"
                                :to="'/scholaryears_edit/' + scholaryear.id + '/'"
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
                </BRow>
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
            scholaryearEntries: [],
            scholaryearEntriesCount: 0,
        };
    },
    methods: {
        loadEntries: function () {
            axios.get("/report/scholaryear/")
                .then((response) => {
                    console.log(response);
                    this.scholaryearEntries = response.data;
                    this.scholaryearEntriesCount = response.data.lenght;
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
