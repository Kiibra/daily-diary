from django.shortcuts import render
# Add the HttpResponse
from django.http import HttpResponse


class Dairy:  # Note that parens are optional if not inheriting from another class
  def __init__(self, created_at, title, content, updated_at):
    self.created_at = created_at
    self.title = title
    self.content = content
    self.updated_at = updated_at

diaries = [
  Dairy('06/01/2024', 'thoughts', 'today i am learning and building my first django app.', '06/01/2024' ),
  Dairy('05/20/2014', 'my day', 'today was such a rainy and sad day. I stayed in all day!', '05/31/2024' ),
]


# Create your views here.

# Define the home view
def home(request):
  return HttpResponse('<h1>Welcome to Daily Diary! 🦋</h1>')

# Define the About view
def about(request):
    return render(request, 'about.html')

# Add new view
def diary_index(request):
  return render(request, 'diaries/index.html', { 'diaries': diaries })