from django.db import models
# from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


class Student(models.Model):
    TypeGender = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]
    
    AvailableDepartment = [
        ('CS', 'CS'),
        ('DS', 'DS'),
        ('IT', 'IT'),
        ('AI', 'AI'),
        ('IS', 'IS')
    ]

    name = models.CharField(max_length=50, null=True)
    collegeID = models.CharField(max_length=8, null=True)
    dob = models.DateField(null=True)
    gpa = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    gender = models.CharField(max_length=6, null=True)
    level = models.IntegerField(null=True)
    status = models.BooleanField(default=False, null=True)
    department = models.CharField(max_length=2, null=True)
    email = models.CharField(max_length=50, null=True)
    mobile = models.CharField(max_length=11, null=True)

    class Meta:
        ordering = ['gpa', 'name']

    def __str__(self):
        return self.name
