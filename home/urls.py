from django import views
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
   path('', views.index, name="home"),
   path('login/', views.signin, name="login"),
   path('logout/', views.logoutUser, name="logout"),
   path('signup/', views.signup, name="signup"),
]
