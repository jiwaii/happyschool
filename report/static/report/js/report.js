import { createApp } from "vue";
import { createBootstrap } from "bootstrap-vue-next";

import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue-next/dist/bootstrap-vue-next.css";
import router from "./router/index.js";

import ReportVue from "./ReportPage.vue";

const app = createApp(ReportVue);

app.use(router);
app.use(createBootstrap());
// app.use(pinia);
app.mount("#vue-app");
