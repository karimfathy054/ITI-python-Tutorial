
from django.urls import path
from .views import movies,movie_details
urlpatterns = [
path('movies/',movies),
path('movies/<int:id>/',movie_details)
]