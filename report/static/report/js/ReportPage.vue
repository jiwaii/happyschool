<template>
    <div style="background-image: linear-gradient(180deg,#579fd1,#eaf3fc);padding: 1%; min-height: 700px;">
        <!-- <app-menu
            :menu-info="menuInfo"
        /> -->
        <BBreadcrumb :items="menuBread"/>

        <router-view v-slot="{ Component}">
            <Transition name="fade">
                <component :is="Component" />
            </Transition>
        </router-view>
    </div>
        <router-link
            to="/"
            style="text-decoration: none;"
            >
            Retour menu principale</router-link>
</template>
<script>
import Menu from "@s:core/js/common/menu_bar.vue";
import {BToast} from 'bootstrap-vue-next'

export default {
    data: function () {
        return {
            menuInfo: {},
        };
    },
    mounted: function() {
        // eslint-disable-next-line no-undef
        this.menuInfo = menu;
        this.menuBread = "Menu Principale";
    },
    components: {
        "app-menu": Menu,
    }
};
</script>
