
from django.db import models
class abstractModel(models.Model):
    num = models.IntegerField()
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=50)

    class Meta:
        abstract = True

class Student(abstractModel):
    marks = models.IntegerField()

    def __str__(self):
        return self.name

class Employee(abstractModel):
    salary = models.IntegerField()

    def __str__(self):
        return self.name

