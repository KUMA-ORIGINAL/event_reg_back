# myapp/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterTeamView

router = DefaultRouter()
router.register(r'register', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]