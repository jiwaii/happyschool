<template>
    <div>
        <!-- <app-menu
            :menu-info="menuInfo"
        /> -->
        
        <router-view v-slot="{ Component }">
            <Transition name="fade">
                <component :is="Component" />
            </Transition>
        </router-view>
    </div>
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
    },
    components: {
        "app-menu": Menu,
    }
};
</script>
