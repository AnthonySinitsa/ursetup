from django.urls import path
from .views import SignUpView
from django.contrib.auth import views as auth_views
from web_app.views import home

urlpatterns = [
  path('', home, name='home'),
  path('signup/', SignUpView.as_view(), name='signup'),
  path('login/', auth_views.LoginView.as_view(), name='login'),
  path('logout/', auth_views.LoginView.as_view(), name='logout'),
]