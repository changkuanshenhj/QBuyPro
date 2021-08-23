from django.urls import path

from .views import LoginView, UserAPIView

from .views import user_api, user_api_detail

app_name = 'user'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('api/', user_api, name='api'),
    path('api_1/', UserAPIView.as_view(), name='api_1'),
    path('api/<int:pk>', user_api_detail, name='api_detail'),
]
