from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from .views import PropertyCreateView


urlpatterns = [
  # path('', views.home, name='home'),
  path('', views.home.as_view(), name='home'),
  path('login', views.login, name='login'),
  # path('login', auth_views.LoginView.as_view(),name='login'),
  # path('logout', auth_views.LogoutView.as_view(),name='logout'),
  path('logout', views.logout, name='logout'),
  path('<int:pk>', views.detail.as_view(), name='detail'),
  path('update/<int:pk>', views.update.as_view(), name='update'),
  path('delete/<int:pk>', views.delete.as_view(), name='delete'),
  path('register', views.register, name='register'),
  # path('profile', views.profile, name='profile'),
  path('create',PropertyCreateView.as_view(), name='create'),

]