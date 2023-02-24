from rest_framework.routers import SimpleRouter, DefaultRouter
from django.urls import include, path
from cats.views import CatViewSet

# router = SimpleRouter()
router = DefaultRouter()
router.register('cats', CatViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
