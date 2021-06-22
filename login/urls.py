from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
#router.register(r'heroes', views.HeroViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('login',views.login,name="login or register")
]
