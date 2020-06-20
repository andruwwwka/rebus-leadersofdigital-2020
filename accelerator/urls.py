from django.urls import path

from .resources.tender import TenderViewSet


tender_list = TenderViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = [
    path('tenders/', tender_list, name='tender-list'),
]
