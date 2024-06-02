from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # route for diaries index
    path('diaries/', views.diary_index, name='diary-index'),
    # new route for details 
    path('diaries/<int:diary_id>/', views.diary_detail, name='diary-detail'),
    # new route to show a form and create a diary
    path('diary/create/', views.DiaryCreate.as_view(), name='diary-create'),
]
