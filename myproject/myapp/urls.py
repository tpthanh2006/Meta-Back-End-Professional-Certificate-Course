from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about),
    #path('home/', views.form_view, name="home"),
    #path('booking/', views.form_view),
]