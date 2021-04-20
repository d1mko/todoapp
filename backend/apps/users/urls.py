from django.urls import path
from . import views

urlpatterns = [
    path('authenticated', views.CheckAuthenticatedView.as_view()),
    path('register', views.RegisterView.as_view()),
    path('login', views.LoginView.as_view()),
    path('logout', views.LogoutView.as_view()),
    path('csrf_cookie', views.GetCSRFToken.as_view())
]
