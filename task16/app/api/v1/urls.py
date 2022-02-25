from django.urls import path
from app.api.v1.viewsets import UserProfileViewSet
from rest_framework.routers import DefaultRouter
from dj_rest_auth.registration.views import RegisterView
from django_rest_passwordreset.views import ResetPasswordValidateTokenViewSet, ResetPasswordConfirmViewSet, \
    ResetPasswordRequestTokenViewSet
from dj_rest_auth.views import LoginView, LogoutView

router = DefaultRouter()
router.register('userprofile', UserProfileViewSet),
router.register('password_reset', ResetPasswordRequestTokenViewSet, basename='reset-password-request')
router.register('password_reset/validate_token', ResetPasswordValidateTokenViewSet, basename='reset-password-validate')
router.register('password_reset/confirm', ResetPasswordConfirmViewSet, basename='reset-password-confirm')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]

urlpatterns += router.urls
