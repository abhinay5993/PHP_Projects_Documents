from django.shortcuts import render

# Create your views here.
def todoFrom_indexTemplets(request):
    return render(request, "todo_index.html")