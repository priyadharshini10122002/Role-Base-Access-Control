from django.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import NewsViewSet

from .models import News

router = DefaultRouter()
router.register(r'news', NewsViewSet, basename='news')
urlpatterns = [
    path('', include(router.urls)),
]
