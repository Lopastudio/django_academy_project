from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)


class Lecture(models.Model):
    name = models.CharField(max_length=50)
    theme = models.CharField(max_length=250)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    #test = models.ManyToManyField
    #test2 = models.OneToOneField
