from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    place = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    salary = models.IntegerField()
    contact = models.IntegerField()
    email = models.EmailField(max_length=100)

    def __str__(self):
        return f"{self.Name} - {self.Age}- {self.place}- {self.job} - {self.salary} - {self.contact}- {self.email}"
