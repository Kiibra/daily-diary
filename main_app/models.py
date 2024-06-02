from django.db import models
# Import the reverse function
from django.urls import reverse

# Create your models here.

class Diary(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField(max_length=500)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)

	# ovverride __str__ method to return the diary title attribute
  def __str__(self):
    return self.title
  
  # Add this class method
  def get_absolute_url(self):
    return reverse('diary-detail', kwargs={'diary_id': self.id})