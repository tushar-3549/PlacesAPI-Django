from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'districts', DistrictViewSet)
router.register(r'subdistricts', SubDistrictViewSet)
router.register(r'unions', UnionViewSet)
router.register(r'semimetros', SemiMetroAreaViewSet)

urlpatterns = [
    path("register_user/", register_user, name="register_user"),
    path("places/", PlaceNestedView.as_view(), name="place-nested-api"),
    path("", include(router.urls)),
]