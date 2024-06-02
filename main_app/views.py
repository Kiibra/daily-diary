from django.shortcuts import render
# Add the CreateView
from django.views.generic.edit import CreateView
from .models import Diary


# Create your views here.

# Define the home view
def home(request):
  return render(request, 'home.html')

# Define the About view
def about(request):
    return render(request, 'about.html')

def diary_index(request):
  diaries = Diary.objects.all()
  return render(request, 'diaries/index.html', { 'diaries': diaries })

def diary_detail(request, diary_id):
  diary = Diary.objects.get(id=diary_id)
  return render(request, 'diaries/detail.html', { 'diary': diary })

class DiaryCreate(CreateView):
  model = Diary
  fields = ['title', 'content']