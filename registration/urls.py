from django.conf.urls import url
from django.urls import path, include

from .views import *


app_name = 'registration'


urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='registration'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('profile/', CurrentUserView.as_view(), name='profile'),
    path('list/', UserRetrieveUpdateAPIView.as_view(), name='users_list'),
    path('update/', UserUpdateAPIView.as_view(), name='update_user'),
    path('password-reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('search/', UserListAPIView.as_view(), name='user-search'),

    # # email verification
    # url(r'backend/activate/(?P<uid64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     activate, name='activate'),
]
