from django.urls import path
from . import views

# or from .views import *

urlpatterns = [
    # path('', views.index, name='home'),
    path('', views.HomeTask.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('category/<int:pk>/', views.ViewTask.as_view(), name='category'),
    path('add-task/', views.CreateTask.as_view(), name='add_task'),
]
