from django.db import models

# Create your models here.

class Diary(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField(max_length=500)
  created_at = models.DateField.auto_now_add()
  updated_at = models.DateField.auto_now()