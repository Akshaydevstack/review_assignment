from django.db import models

# Create your models here.

class Auther(models.Model):
    name= models.CharField(max_length=100)
    wirting_name= models.CharField(max_length=100)
    date_of_birth= models.DateField()

    def __str__(self):
        return self.name

class Books(models.Model):
    Book_title= models.CharField(max_length=100)
    Publish_date= models.DateField()
    auther= models.ForeignKey(Auther,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Book_title


class members(models.Model):
    name= models.CharField(max_length=100)
    email= models.EmailField()
    join_date= models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name
