from api.views import SignupUser, TokenUser
from django.urls import path

urlpatterns = [
    path('signup/', SignupUser),
    path('token/', TokenUser),
]
