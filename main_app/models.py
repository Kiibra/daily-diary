from django.db import models

# Create your models here.

class Diary(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField(max_length=500)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)

	# ovverride __str__ method to return the diary title attribute
  def __str__(self):
    return self.title