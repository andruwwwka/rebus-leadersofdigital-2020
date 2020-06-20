from rest_framework.routers import DefaultRouter

from .resources.tender import TenderViewSet

router = DefaultRouter()
router.register(r'tenders', TenderViewSet, basename='tenders')
urlpatterns = router.urls
