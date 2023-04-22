from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_login(request):
    html = "<html><body>you are hitting the hello_login() from appmod1_login view ! </body></html>" 
    return HttpResponse(html)

def mySign_page(request):
    return render(request, "loginPage.html")