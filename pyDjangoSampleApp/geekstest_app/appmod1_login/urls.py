from django.urls import path
# from . import views
from appmod1_login.views import hello_login

urlpatterns = [
    path('hello-signin',hello_login),
]