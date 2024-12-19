from django.urls import path

from .views import LoginAPI, RegisterAPI

urlpatterns = [
    # crendentials auth
    path("register", RegisterAPI.as_view(), name="register"),
    path("login", LoginAPI.as_view(), name="login"),
]
