from django.urls import path
from .views import *

app_name = 'user'

urlpatterns = [
    path("", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("signup/", signup_view),
    path("verification/", verification_view, name="verification"),
]
