from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AgentViewSet, CustomAuthToken, UserInfoView, AgentMissionsView, MissionViewSet, change_password

router = DefaultRouter()
router.register(r'agents', AgentViewSet)
router.register(r'missions',MissionViewSet)

urlpatterns = [
    path('auth/login/', CustomAuthToken.as_view(), name='api_token_auth'),
    path('auth/user/', UserInfoView.as_view(), name='user_info'),
    path('agent/missions/', AgentMissionsView.as_view(), name='agent_missions'),
    path('auth/change-password/', change_password, name='change-password'),
] + router.urls
