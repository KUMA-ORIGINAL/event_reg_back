from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterTeamView, TeamListView

router = DefaultRouter()
router.register(r'register-team', RegisterTeamView, basename='register_team')
router.register(r'teams', TeamListView, basename='team-list')

urlpatterns = [
    path('', include(router.urls)),
]