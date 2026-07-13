from django.db import models
from django.db.models import Q
from django.contrib.auth.models import Group
from core.models import (
    GivenCourseModel,
    StudentLevelModel,
    ScholarYearModel,
    ClasseGroupModel,
    CourseModel,
)
from core.templatetags import scholar_year

# Create your models here.


class PeriodModel(models.Model):
    # period_num = models.PositiveSmallIntegerField() #Deprecated
    period_label = models.CharField(max_length=200, default="P")
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
                fields=["period_label", "classe_group", "scholar_year"],
                violation_error_message="Cette periode existe déjà",
            ),
        ]


class CotationModel(models.Model):
    title = models.CharField()
    max_note = models.DecimalField(decimal_places=2,max_digits=5)
    made_date = models.DateField()
    given_course = models.ForeignKey(GivenCourseModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} {self.made_date} ({self.max_note} points)"


class NoteModel(models.Model):
    note = models.DecimalField(default=0,decimal_places=2, max_digits=5)
    comment = models.CharField(null=True,blank=True)
    cotation = models.ForeignKey(CotationModel, on_delete=models.CASCADE)
    student_level = models.ForeignKey(StudentLevelModel, on_delete=models.CASCADE)
    
    @property
    def student_name(self):
        return f"{self.student_level.student.first_name} {self.student_level.student.last_name}"
   
    @property
    def max_note(self):
        return self.cotation.max_note


# class PeriodCommentModel(models.Model):
#     student_level = models.ForeignKey(StudentLevelModel, on_delete=models.CASCADE)
#     period = models.ForeignKey(PeriodModel, on_delete=models.CASCADE)
#     course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
#     comment = models.CharField()
