from django.urls import path
from djtodo_app.views import todoFrom_indexTemplets

urlpatterns = [
    path('play-todoapp',todoFrom_indexTemplets)
]