from django.shortcuts import render
from .models import Diary


class Diary:  # Note that parens are optional if not inheriting from another class
  def __init__(self, created_at, title, content, updated_at):
    self.title = title
    self.content = content
    self.created_at = created_at
    self.updated_at = updated_at

diaries = [
  Diary('06/01/2024', 'thoughts', 'today i am learning and building my first django app.', '06/01/2024' ),
  Diary('05/20/2014', 'my day', 'today was such a rainy and sad day. I stayed in all day!', '05/31/2024' ),
]


# Create your views here.

# Define the home view
def home(request):
  return render(request, 'home.html')

# Define the About view
def about(request):
    return render(request, 'about.html')

# Add new view
def diary_index(request):
  # diaries = Diary.objects.all()
  return render(request, 'diaries/index.html', { 'diaries': diaries })

def diary_detail(request, diary_id):
  diary = Diary.objects.get(id=diary_id)
  return render(request, 'diaries/detail.html', { 'diary': diary })