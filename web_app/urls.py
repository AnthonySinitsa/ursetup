from django.urls import path
from .views import SignUpView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from .views import home, AddSetupView, FavoritesView

urlpatterns = [
  path('', home, name='home'),
  path('signup/', SignUpView.as_view(), name='signup'),
  path('login/', auth_views.LoginView.as_view(), name='login'),
  path('logout/', auth_views.LoginView.as_view(), name='logout'),
  path('add-setup/', AddSetupView.as_view(), name='add_setup'),
  path('favorites/', FavoritesView.as_view(), name='favorites'),
  path('logout/', LogoutView.as_view(), name='logout'),
]