from django.urls import path, include
from jakalapp.views import show_jakal, show_how_to_play

urlpatterns = [
    path('', show_jakal, name="main"),
    path('\how_to_play', show_how_to_play, name='play')
] 