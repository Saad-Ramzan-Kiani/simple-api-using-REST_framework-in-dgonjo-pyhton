from django.urls import path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import YourModelViewSet  # Replace YourModelViewSet with your actual viewset  



router = DefaultRouter()
router.register(r'yourmodel', YourModelViewSet)

urlpatterns = [
    path('home', views.home, name='home'),
    path('', include(router.urls)),
]



