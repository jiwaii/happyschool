<template>
    <div>
        <div>
            <b-card
                overlay
                img-src="/static/report/img/headbar.png"
                img-alt="Card Image"
                style="margin-bottom: 1%; height: 100px ;"
                text-variant="white"
                title="Bulletins ISLN"
            />
        </div>


        <!-- <span>Message : {{ test }} </span> -->
        <b-container :fluid="fullscreen">
            <b-row>
                <b-col>
                    <div>
                        <a href="http://">
                            <b-card
                                overlay
                                title="Cours"
                                img-src="/static/report/img/stains-purple-courses.jpg"
                                img-alt="Image"
                                img-top
                                style="max-width: 20rem;color: black;text-align: center;"
                                class="mb-2"
                                footer="Pour gérer des cours et des cotations."
                            />
                        </a>
                    </div>
                </b-col>
                <b-col>
                    <div>
                        <router-link
                            to="/periods/"
                        >
                            <b-card
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
                </b-col>
                <b-col>
                    <div>
                        <router-link
                            to="/"
                        >
                            <b-card
                                overlay
                                title="Élèves"
                                img-src="/static/report/img/stains-purple-students.jpg"
                                img-alt="Image"
                                img-top
                                tag="article"
                                style="max-width: 20rem;color: black;text-align: center;"
                                class="mb-2"
                                footer="Pour gérer un à plusieurs années d'études d'un élève"
                            />
                        </router-link>
                    </div>
                </b-col>
            </b-row>
            <b-row>
                <b-col>
                    <div>
                        <router-link
                            to="/scholaryears/"
                        >
                            <b-card
                                to="/scholaryears/"
                                overlay
                                title="Années Scolaires"
                                img-src="/static/report/img/stains-blue-scholaryear.jpg"
                                img-alt="Image"
                                img-top
                                style="max-width: 20rem;color: black;text-align: center;"
                                class="mb-2"
                                footer="Créer une année scolaire ou mettre à jour"
                            />
                        </router-link>
                    </div>
                </b-col>
                <b-col />
                <b-col />
            </b-row>
        </b-container>
    </div>
</template>
<script>
// import { RouterLink } from "vue-router";

export default{
    data: function(){
        return {
            // test : "hello"
        };
    },
};
</script>
