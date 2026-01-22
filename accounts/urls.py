from django.urls import path
from .views import UserregistrationView

urlpatterns = [
    path("register/",UserregistrationView.as_view(),name='User Registration')
]
