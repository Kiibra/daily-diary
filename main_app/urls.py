from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # route for diaries index
    path('diaries/', views.diary_index, name='diary-index'),
]
