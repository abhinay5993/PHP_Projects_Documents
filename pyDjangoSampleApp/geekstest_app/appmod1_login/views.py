from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from appmod1_login.models import PersonModel
from hashids import Hashids

# Create your views here.
def hello_login(request):
    html = "<html><body>you are hitting the hello_login() from appmod1_login view ! </body></html>" 
    return HttpResponse(html)

def mySign_page(request):
    return render(request, "loginPage.html")

def get_person_details(request,encrypted_id):
    hashids = Hashids(salt=settings.PRIVATE_KEY)
    decrypted_id = hashids.decode(encrypted_id)[0]
    print("decrypted id", decrypted_id)
    person_object = PersonModel.objects.get(id=decrypted_id)
    my_data = {
        "Fname" : person_object.fname,
        "Lname" : person_object.lstName,
        "email" : person_object.emailVal
    }
    return render(request, "person_info.html", my_data)