from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserAPIView.as_view(), name="create_user"),
    path('token/', views.CreateTokenAPIView.as_view(), name="token"),
    path('me/', views.ManageUserAPIView.as_view(), name='me')
]