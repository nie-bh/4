from django.urls import path

from .views import UserSigninView, UserSignoutView, dashboard_view, user_signup

urlpatterns = [
    path("signup/", user_signup, name="user_signup"),
    path("signin/", UserSigninView.as_view(), name="user_signin"),
    path("signout/", UserSignoutView.as_view(), name="user_signout"),
    path("dashboard/", dashboard_view, name="dashboard"),
]
