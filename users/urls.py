from django.urls import path

from .resources import Login

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
]
