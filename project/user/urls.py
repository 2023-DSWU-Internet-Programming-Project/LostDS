from django.urls import path
from .views import *

urlpatterns = [
    path("", login_view),
    path("logout/", logout_view),
]
