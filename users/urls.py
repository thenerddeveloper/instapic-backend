from django.urls import include,path
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('register', views.RegisterApi.as_view()),
    path('', include(router.urls)),
]