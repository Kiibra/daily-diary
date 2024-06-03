from django.shortcuts import render, redirect
# Add the CreateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Diary
from django.contrib.auth.views import LoginView
# Add the two imports below
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


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
  
  # This inherited method is called when a
  # valid diary form is being submitted
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the diary
    # Let the CreateView do its job as usual
    return super().form_valid(form)


class DiaryUpdate(UpdateView):
  model = Diary
  # Let's disallow the renaming of a diary by excluding the name field!
  fields = ['title', 'content']

class DiaryDelete(DeleteView):
  model = Diary
  success_url = '/diaries/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in
      login(request, user)
      return redirect('diary-index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
  # Same as: return render(request, 'signup.html', {'form': form, 'error_message': error_message})