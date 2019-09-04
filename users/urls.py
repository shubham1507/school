from rest_framework import routers
from users.views import UserViewSet, UserViewSet2
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'users2', UserViewSet2)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_auth.urls')),
]