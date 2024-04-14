from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

# Create a router and register our viewsets with it.
post_router = DefaultRouter()
post_router.register(r'posts', PostViewSet, basename='post')  # Specify basename='post'

# The API URLs are now determined automatically by the router.
urlpatterns = post_router.urls