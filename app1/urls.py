from django.urls import path
from .import views
from django.conf.urls import url
urlpatterns = [
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('form/', views.form, name="form"),
    path('table/', views.table, name = 'table'),
    path('edit/<int:pk>/', views.post_edit ,name="post_edit"),
    path('delete/<int:pk>/', views.delete ,name="delete"),
    
]
