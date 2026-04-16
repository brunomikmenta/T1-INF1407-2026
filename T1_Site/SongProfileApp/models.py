from django.db import models

# Create your models here.

GENDER_CHOICES = [
    ('M', 'Masculino'),
    ('F', 'Feminino'),
    ('O', 'Outro'),
    ('N', 'Prefiro não dizer'),
]

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices = GENDER_CHOICES)
    email = models.EmailField(max_length=254, unique=True)
    senha = models.CharField(max_length=15)
  

    def __str__(self):
        return self.username