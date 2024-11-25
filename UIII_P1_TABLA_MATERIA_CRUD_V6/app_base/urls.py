from django.urls import path
from app_base import views

urlpatterns={
        # inicio miniso
    path('', views.inicio),
}