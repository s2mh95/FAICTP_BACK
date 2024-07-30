from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AgentViewSet, CustomAuthToken, UserInfoView

router = DefaultRouter()
router.register(r'agents', AgentViewSet)

urlpatterns = [
    path('auth/login/', CustomAuthToken.as_view(), name='api_token_auth'),
    path('auth/user/', UserInfoView.as_view(), name='user_info'),
] + router.urls