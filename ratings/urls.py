from rest_framework.routers import DefaultRouter

from .resources.badge import BadgeViewSet
from .resources.history import HistoryViewSet
from .resources.reward import RewardViewSet

router = DefaultRouter()
router.register(r'rewards', RewardViewSet, basename='rewards')
router.register(r'badges', BadgeViewSet, basename='badges')
router.register(r'history', HistoryViewSet, basename='history')
urlpatterns = router.urls
