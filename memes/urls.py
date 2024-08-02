from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MemeViewSet
from memes.apps import MemesConfig

app_name = MemesConfig.name

router = DefaultRouter()
router.register(r'', MemeViewSet, basename='memes')

urlpatterns = [
    path('', include(router.urls)),
]
