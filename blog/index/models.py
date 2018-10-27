from django.db import models

# Create your models here.


class User(models.Model):
   email = models.EmailField(null=True, verbose_name='邮件')
   password = models.CharField(max_length=200)

   
