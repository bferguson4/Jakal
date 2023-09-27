from django.urls import path, include
from jakalapp.views import show_jakal

urlpatterns = [
    path('', show_jakal, name="main"),
] 