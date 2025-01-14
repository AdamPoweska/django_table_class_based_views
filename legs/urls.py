from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='hello'),
    path('create/', views.CreateRecord.as_view(), name='create'),
    path('update_view/<int:pk>/', views.TableUpdateView.as_view(), name='update'),
    path('read/', views.TableListView.as_view(), name='read'),
    path('delete_view/<int:pk>', views.TableDeleteView.as_view(), name='delete'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
