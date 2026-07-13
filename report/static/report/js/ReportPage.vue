<template>
    <app-menu
        :menu-info="menuInfo"
    />
    <BApp>
        <div style="background-image: linear-gradient(180deg,#579fd1,#eaf3fc);padding: 1%; min-height: 700px;">
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
            Retour menu principal
        </router-link>
    </BApp>
</template>
<script>
import Menu from "@s:core/js/common/menu_bar.vue";

export default {
    data: function () {
        return {
            menuInfo: {},
        };
    },
    mounted: function () {
        // eslint-disable-next-line no-undef
        this.menuInfo = menu;
    },
    components: {
        "app-menu": Menu,
    },
};
</script>
