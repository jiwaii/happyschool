<template>
    
        <div style="position: fixed; right: 50px;left: 50px;">
            <b-img src="/static/report/img/logo_isln_bleu_Only.png" placement="center" fluid alt=""/>
        </div>


        <!-- <span>Message : {{ test }} </span> -->
        <b-container :fluid="fullscreen">
            <b-row>
                <b-col>
                    <div>
                        <router-link
                            to="/"
                            style="text-decoration: none;">
                            <b-card
                                
                                title="Cours"
                                img-src="/static/report/img/stains-purple-courses.jpg"
                                img-alt="Image"
                                img-top
                                style="max-width: 20rem;color: black;text-align: center;"
                                class="mb-2"
                                footer="Pour gérer des cours et des cotations."
                            >
                        </b-card>
                    </router-link>
                    </div>
                </b-col>
                <b-col>
                    <div>
                        <router-link
                            to="/periods/"
                            style="text-decoration: none;"
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
                            style="text-decoration: none;"
                        >
                            <b-card
                                overlay
                                title="Élèves"
                                img-src="/static/report/img/stains-blue-students.jpg"
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
                            style="text-decoration: none;"
                        >
                            <b-card
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
                <b-col>
                    <div>
                        <router-link
                            to="/grouped_classe/"
                            style="text-decoration: none;"
                        >
                            <b-card
                                overlay
                                title="Classes"
                                img-src="/static/report/img/stains-purple-classes.jpg"
                                img-alt="Image"
                                img-top
                                style="max-width: 20rem;color: black;text-align: center;"
                                class="mb-2"
                                footer="Gestion des classes et des groupes de classes"
                            />
                        </router-link>
                    </div>
                </b-col>
                <b-col>
                    <div>
                        <router-link
                            to="/"
                            style="text-decoration: none;"
                        >
                            <b-card
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
                </b-col>
            </b-row>
        </b-container>
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
