from django.urls import path
from . import views


urlpatterns = [
    path('', views.homeView, name='home'),
    path("register/", views.registerRequest, name="register"),
    path("login/", views.loginRequest, name="login"),
    path("logout", views.logoutRequest, name="logout"),
    path("news/", views.newsRequest, name='news'),
]
