from django.shortcuts import render
# Add the HttpResponse
from django.http import HttpResponse


# Create your views here.

# Define the home view
def home(request):
  return HttpResponse('<h1>Welcome to your Daily Diaries 🦋</h1>')