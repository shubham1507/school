from rest_framework import routers
from users.views import TeacherViewSet, StudentViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from users import views
router = routers.DefaultRouter()
router.register(r'teacher', views.TeacherViewSet),
router.register(r'student', views.StudentViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('auth/', include('rest_auth.urls')),
]

urlpatterns += router.urls
