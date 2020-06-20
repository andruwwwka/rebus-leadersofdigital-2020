from rest_framework.routers import DefaultRouter

from .resources.team import TeamViewSet
from .resources.tender import TenderViewSet

router = DefaultRouter()
router.register(r'tenders', TenderViewSet, basename='tenders')
router.register(r'teams', TeamViewSet, basename='teams')
urlpatterns = router.urls
