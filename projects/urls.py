from django.urls import path, include
from rest_framework import routers
from projects.views import ProfileViewSet, ProjectViewSet, CertificateViewSet, CertifyingInstitutionViewSet

router = routers.DefaultRouter()
router.register(r"profiles", ProfileViewSet)
router.register(r"projects", ProjectViewSet)
router.register(r"certificates", CertificateViewSet)
router.register(r"certifying-institutions", CertifyingInstitutionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
