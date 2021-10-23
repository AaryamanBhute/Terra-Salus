from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name="homepage"),
    path('about', views.about, name="aboutpage"),
    path('contact', views.contact, name="contactpage"),
    path('leadership', views.leadership, name="leadershippage"),
    path('join', views.join, name="joinpage"),
]