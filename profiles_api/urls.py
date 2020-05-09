from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('hellow-viewset', views.HelloViewSet, base_name="hello_viewset")
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiVIew.as_view()),
    path('', include(router.urls)),
]
