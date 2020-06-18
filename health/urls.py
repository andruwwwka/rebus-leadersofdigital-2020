from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .resources import Health

urlpatterns = [
    path('', Health.as_view()),
]
