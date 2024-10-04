from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterTeamView

router = DefaultRouter()
router.register(r'register-team', RegisterTeamView, basename='register_team')

urlpatterns = [
    path('', include(router.urls)),
]