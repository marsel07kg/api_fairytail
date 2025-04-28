from django.urls import path
from . import views


urlpatterns = [
    path('', views.CharacterView.as_view()),

]