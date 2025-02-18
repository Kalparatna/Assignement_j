from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, PatientViewSet, HeartRateViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'heart_rate', HeartRateViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
