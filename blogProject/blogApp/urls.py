from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='home'),
    path('create/', views.post_create, name='post_create'),
    path('<int:post_id>/', views.post_detail, name='post_detail'), 
]