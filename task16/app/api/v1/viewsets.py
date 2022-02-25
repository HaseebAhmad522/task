from rest_framework.viewsets import ModelViewSet
from app.api.v1.serializer import UserSerializer
from app.models import CustomUser
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
User = get_user_model()


class UserProfileViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CustomUser.objects.filter(id=self.request.user.id)
        return queryset
