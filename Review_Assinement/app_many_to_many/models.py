from django.db import models

# Create your models here.

class Coures(models.Model):
    coures_name= models.CharField(max_length=25)

    def __str__(self):
        return self.coures_name
    
class Student(models.Model):
    student_name= models.CharField(max_length=50)
    join_date= models.DateField(auto_created=True)
    coures= models.ManyToManyField(Coures, related_name='student')

    def __str__(self):
        return self.student_name