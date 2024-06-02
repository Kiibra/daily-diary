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
    # Add the new routes for update and delete
    path('diaries/<int:pk>/update/', views.DiaryUpdate.as_view(), name='diary-update'),
    path('diaries/<int:pk>/delete/', views.DiaryDelete.as_view(), name='diary-delete'),
]
