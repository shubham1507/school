from rest_framework import viewsets

from users.models import User
from users.serializers import UserSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_context(self):
        return {'request': self.request, 'context': 'teacher'}


class StudentViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_context(self):
        return {'request': self.request, 'context': 'student'}
