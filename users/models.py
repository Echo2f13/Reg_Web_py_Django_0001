from django.db import models

class Member(models.Model):
  username = models.CharField(max_length=16,unique=True,null=True)
  password = models.CharField(max_length=35)
  phone_num = models.IntegerField(max_length=255)
  gender = models.CharField(max_length=6)

  def __str__(self) :
    return self.username