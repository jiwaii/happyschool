<template>
    <!-- <div style="position: fixed; right: 50px;left: 50px;">
            <b-img src="/static/report/img/logo_isln_bleu_Only.png" placement="center" fluid alt=""/>
        </div> -->

    <!-- <span>Message : {{ test }} </span> -->
    <BContainer :fluid="fullscreen">
        <BRow>
            <BCol>
                <div>
                    <router-link
                        to="/givencourse/"
                        style="text-decoration: none;"
                    >
                        <BCard

                            title="Mes cours"
                            img-src="/static/report/img/stains-purple-courses.jpg"
                            img-alt="Image"
                            img-top
                            style="max-width: 20rem;color: black;text-align: center;"
                            class="mb-2"
                            footer="Pour gérer des cours et des cotations."
                        />
                    </router-link>
                </div>
            </BCol>
            <BCol>
                <div>
                    <router-link
                        to="/periods/"
                        style="text-decoration: none;"
                    >
                        <BCard
                            overlay
                            title="Périodes"
                            img-src="/static/report/img/stains-blue-periods.jpg"
                            img-alt="Image"
                            img-top
                            tag="article"
                            style="max-width: 20rem;color: black;text-align: center;"
                            class="mb-2"
                            footer=" Pour gérer des périodes"
                        />
                    </router-link>
                </div>
            </BCol>
            <BCol>
                <div>
                    <router-link
                        to="/"
                        style="text-decoration: none;"
                    >
                        <BCard
                            overlay
                            title="Bulletins"
                            img-src="/static/report/img/stains-blue-reports.jpg"
                            img-alt="Image"
                            img-top
                            style="max-width: 20rem;color: black;text-align: center"
                            class="mb-2"
                            footer="Obtenir le bulletin d'un élève ou d'une classe"
                        />
                    </router-link>
                </div>
            </BCol>
        </BRow>
    </BContainer>
</template>
<script>

export default {
    data: function () {
        return {
        };
    },
};
</script>
