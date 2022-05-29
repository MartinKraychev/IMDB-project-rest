from django.urls import path, include
from rest_framework import routers

from Movies.user_auth.views import RegisterViewSet, LoginView, LogoutView

router = routers.DefaultRouter()

router.register(r'register', RegisterViewSet, 'register')

urlpatterns = (
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include(router.urls)),
)
