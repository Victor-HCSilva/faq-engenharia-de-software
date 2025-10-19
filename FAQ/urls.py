from django.urls import path
from FAQ.views import main

urlpatterns= [
    path('', main, name="main")
]
