from django.urls import path
# from . import views
from appmod1_login.views import get_person_details, hello_login, mySign_page

urlpatterns = [
    path('hello-signin',hello_login),
    path('my-login',mySign_page), 
    path('persondetails/<str:encrypted_id>',get_person_details), 
]