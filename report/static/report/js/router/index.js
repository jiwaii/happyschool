// This file is part of Happyschool.
//
// Happyschool is the legal property of its developers, whose names
// can be found in the AUTHORS file distributed with this source
// distribution.
//
// Happyschool is free software: you can redistribute it and/or modify
// it under the terms of the GNU Affero General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// Happyschool is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU Affero General Public License for more details.
//
// You should have received a copy of the GNU Affero General Public License
// along with Happyschool.  If not, see <http://www.gnu.org/licenses/>.


import ReportMenu from "../ReportMenu.vue";
import Report_ScholaryearList from "../Report_ScholaryearList.vue";
import Report_Scholaryear from "../Report_ScholaryearForm.vue";
import Report_PeriodesList from "../Report_PeriodesList.vue";
import Report_PeriodForm from "../Report_PeriodForm.vue";
import Report_ClasseGroup from "../Report_ClasseGroup.vue";
import Report_StudentLevel from "../Report_StudentLevel.vue";
import { createRouter, createWebHashHistory } from "vue-router";

const router = createRouter({
    routes: [
        {
            path: "/",
            component: ReportMenu,
        },
        {
            path: "/scholaryears/",
            component: Report_ScholaryearList,
            props: true
        },
        {
            path: "/scholaryears_form/",
            component: Report_Scholaryear,
            props: true
        },
        {
            path:"/scholaryears_edit/:id",
            component: Report_Scholaryear,
            props: true
        },
        {
            path:"/periods/",
            component: Report_PeriodesList,
            props:true

        },
        {
            path:"/period_form/",
            component: Report_PeriodForm,
            props:true
        },
        {
            path:"/period_edit/:id",
            component: Report_PeriodForm,
            props:true
        },
        {
            path:"/grouped_classe/",
            component: Report_ClasseGroup,
            props:true
        },
        {
            path:"/students_levels/",
            component: Report_StudentLevel,
            props:true
        },
    ],
    history: createWebHashHistory(),
});

export default router;
