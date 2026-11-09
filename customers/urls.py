from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet

router=DefaultRouter()
router.register("Customer",CustomerViewSet)

urlpatterns = router.urls

