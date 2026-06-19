from django.db import models
from django.db.models import Q
from django.contrib.auth.models import Group
from core.models import (
    GivenCourseModel,
    StudentLevelModel,
    ScholarYearModel,
    ClasseGroupModel,
)
from core.templatetags import scholar_year

# Create your models here.



# class ClasseGroup(models.Model):
#     studyYear = models.PositiveSmallIntegerField(null=False, blank=False)
#     title = models.CharField(null=False, blank=False)

#     def __str__(self):
#         return f"{self.studyYear} ({self.title})"


# class ScholarYear(models.Model):
#     label = models.CharField(max_length=9, null=False, blank=False)
#     dateStart = models.DateField(null=False, blank=False)
#     dateEnd = models.DateField(null=False, blank=False)

#     class Meta:
#         constraints = [models.UniqueConstraint("label", name="unique_label")]

#     def __str__(self):
#         return f"{self.label}"


# class Classe(models.Model):
#     classe = models.PositiveSmallIntegerField(null=False, blank=False)
#     letter = models.CharField(max_length=2, blank=False, null=False)
#     classeGroup = models.ForeignKey(
#         ClasseGroup, related_name="classes", on_delete=models.PROTECT, null=True, blank=False
#     )

#     class Meta:
#         constraints = [
#             models.UniqueConstraint(
#                 name="unique_classe", fields=["classe", "letter", "classeGroup"]
#             )
#         ]

#     def __str__(self):
#         return f"{self.classe}{self.letter}"


class PeriodModel(models.Model):
    period_num = models.PositiveSmallIntegerField()
    date_start = models.DateField()
    date_end = models.DateField()
    classe_group = models.ForeignKey(ClasseGroupModel, on_delete=models.CASCADE)
    scholar_year = models.ForeignKey(ScholarYearModel, on_delete=models.CASCADE)

    @property
    def classeGroupLabel(self):
        return f"{self.classe_group.study_year}e année"

    @property
    def order(self):
        periods = PeriodModel.objects.filter(
            scholar_year=self.scholar_year, classe_group=self.classe_group
        ).order_by("date_start")
        position = 0
        for p in periods:
            position += 1
            if p == self:
                return position

    class Meta:
        constraints = [
            models.UniqueConstraint(
                name="unique_period",
                fields=["period_num", "classe_group", "scholar_year"],
                violation_error_message="Cette periode existe déjà",
            ),
        ]

    # def save(self,*args, **kwargs):
    #     overlaped = False
    #     num_of_periods = Period.objects.filter(classeGroup=self.classeGroup,scholarYear=self.scholarYear).count()
    #     period_exist = False if num_of_periods == 0 else True
    #     existingPeriods = Period.objects.filter(classeGroup=self.classeGroup,scholarYear=self.scholarYear).order_by('dateStart')

    #     ## Test Overlaping when have periods
    #     if (period_exist):
    #         for p in existingPeriods:
    #             print(f'p-{p.periodNum}: {p.dateStart} => {p.dateEnd}')
    #             if (self.dateStart >= p.dateStart and self.dateStart <= p.dateEnd) or (self.dateEnd <= p.dateEnd and self.dateEnd >= p.dateStart):
    #                 overlaped = True
    #                 print("overlaps !")
    #                 break
    #         print(f'current insert p-{self.periodNum}: {self.dateStart} => {self.dateEnd}')

    #     else:
    #         print('No periods again')

    #     if (overlaped):
    #         print('400: add or update period error: overlaps dates')
    #         return
    #     else:
    #         return super().save(*args, **kwargs)


# class Course(models.Model):
#     title = models.CharField(max_length=100)
#     hoursPerWeek = models.IntegerField("hoursPerWeek")
#     scholarYear = models.ForeignKey(ScholarYear, null=False, blank=False, on_delete=models.RESTRICT)


class CotationModel(models.Model):
    title = models.CharField()
    max_note = models.IntegerField()
    made_date = models.DateField()
    course = models.ForeignKey(GivenCourseModel, on_delete=models.CASCADE)


# class StudentLevel(models.Model):
#     student = models.ForeignKey(StudentModel, on_delete=models.PROTECT)
#     classe = models.ForeignKey(Classe, on_delete=models.PROTECT)
#     scholarYear = models.ForeignKey(ScholarYear, on_delete=models.PROTECT)

#     class Meta:
#         constraints = [
#             models.UniqueConstraint(
#                 name="unique_studentLevel", fields=["student", "classe", "scholarYear"]
#             )
#         ]

#     def __str__(self):
#         return (
#             f"{self.student.first_name} {self.student.last_name} {self.classe} {self.scholarYear}"
#         )


class NoteModel(models.Model):
    note = models.IntegerField(default=0)
    comment = models.CharField()
    cotation = models.ForeignKey(CotationModel, on_delete=models.CASCADE)
    student_level = models.ForeignKey(StudentLevelModel, on_delete=models.CASCADE)


# class StudentLevelCourse(models.Model):
#     studentLevel = models.ForeignKey(
#         StudentLevel, on_delete=models.CASCADE, null=False, blank=False
#     )
#     course = models.ForeignKey(Course, on_delete=models.CASCADE, null=False, blank=False)
