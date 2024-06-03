from django.shortcuts import render, redirect
# Add the CreateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Diary
from django.contrib.auth.views import LoginView


# Create your views here.

# Define the home view
class Home(LoginView):
  template_name = 'home.html'

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
  success_url = '/diaries/'

class DiaryUpdate(UpdateView):
  model = Diary
  # Let's disallow the renaming of a diary by excluding the name field!
  fields = ['title', 'content']

class DiaryDelete(DeleteView):
  model = Diary
  success_url = '/diaries/'

