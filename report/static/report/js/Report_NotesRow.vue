<script>
export default {
    props: {
        note: JSON,
    },
    methods: {
        // intDecimalParser(value) {

        // },
    },
    data: function () {
        return {
            toIntDecimalParser: (value) => {
                return Intl.NumberFormat("fr-BE", { minimumFractionDigits: 0, maximumFractionDigits: 2 }).format(value).toString();
            },
        };
    },
};
</script>
<template>
    <!-- eslint-disable vue/no-mutating-props -->
    <BRow
        :style="{color: (note.note < note.max_note/2)?'red':'black'}"
        class="note-row"
    >
        <BCol>
            {{ note.student_name }}
            {{ toIntDecimalParser(note.note) }}
        </BCol>
        <BCol
            sm="2"
            lg="2"
        >
            <BFormInput
                :style="{color: (note.note < note.max_note*0.5)?'red':(note.note >= note.max_note*0.75)?'green':'black'}"
                type="number"
                :max="note.max_note"
                min="0"
                v-model="note.note"
                :formatter="toIntDecimalParser()"
            />
        </BCol>
        <BCol
            sm="6"
        >
            <BFormInput
                type="text"
                v-model="note.comment"
            />
        </BCol>
    </BRow>
</template>
<style>
.note-row {
    background-color: #cdd1d6;
    border: 2px #579fd1 solid;
    margin: 2px;
    padding: 0.5%;
    border-radius: 5px;
}
.note-row:hover{
    animation: zoomrow 0.5s none;
    /* font-size: 120% ; */
    font-weight: bold;
    background-color: #e9ecef;

}
@keyframes zoomrow {
    from {
        /* font-size: 100%; */
        font-weight: normal;
        background-color: #cdd1d6;
    }
    to{
        /* font-size: 120%; */
        font-weight: bold;
        background-color: #e9ecef;
    }
}
</style>
