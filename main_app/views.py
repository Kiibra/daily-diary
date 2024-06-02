from django.shortcuts import render
# Add the HttpResponse
from django.http import HttpResponse


# Create your views here.

# Define the home view
def home(request):
  return HttpResponse('<h1>Welcome to Daily Diary! 🦋</h1>')

# Define the About view
def about(request):
    return render(request, 'about.html')