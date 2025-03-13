from django.db import models
from django.contrib.auth.models import Group
from core.models import StudentModel 
# Create your models here.

class ScholarYear(models.Model):
    label = models.CharField(max_length=9,null=False,blank=False)
    dateStart = models.DateField(null=False,blank=False)
    dateEnd = models.DateField(null=False, blank=False)
    
    class Meta:
        constraints = [
            models.UniqueConstraint("label",name="unique_label")
        ]

class ClasseGroup(models.Model):
    studyYear = models.PositiveSmallIntegerField(null=False,blank=False)
    title = models.CharField(null=False,blank=False)

class Classe(models.Model):
    classe = models.PositiveSmallIntegerField(null=False,blank=False)
    letter = models.CharField(max_length=2,blank=False,null=False)

class Period(models.Model):
    periodNum = models.PositiveSmallIntegerField(null=False,blank=False)
    dateStart = models.DateField(null=False,blank=False)
    dateEnd = models.DateField(null=False,blank=False)
    scholarYear = models.ForeignKey(ScholarYear,on_delete=models.CASCADE,null=False,blank=False)

class Course(models.Model):
    title = models.CharField(max_length=100)
    hoursPerWeek = models.IntegerField("hoursPerWeek")
    scholarYear = models.ForeignKey(ScholarYear,null=False,blank=False,on_delete=models.RESTRICT)

class Cotation(models.Model):
    title = models.CharField(null=False,blank=False)
    max_note = models.IntegerField(null=False,blank=False)
    madeDate = models.DateField()
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null=False,blank=False)

class StudentLevel(models.Model):
    student = models.ForeignKey(StudentModel,on_delete=models.PROTECT)
    classe = models.ForeignKey(Classe,on_delete=models.PROTECT)
    scholarYear = models.ForeignKey(ScholarYear,on_delete=models.PROTECT)

class Note(models.Model):
    note = models.IntegerField(null=False,blank=False,default=0)
    comment = models.CharField()
    cotation = models.ForeignKey(Cotation,on_delete=models.CASCADE,null=False,blank=False)
    studentLevel = models.ForeignKey(StudentLevel,on_delete=models.CASCADE)

class StudentLevelCourse(models.Model):
    studentLevel = models.ForeignKey(StudentLevel, on_delete=models.CASCADE,null=False,blank=False)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null=False,blank=False)

