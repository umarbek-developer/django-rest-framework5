from rest_framework.routers import DefaultRouter
from .views import Vazifa5ViewSet

router = DefaultRouter()
router.register('vazifa5', Vazifa5ViewSet)

urlpatterns = router.urls
