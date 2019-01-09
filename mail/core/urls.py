from django.urls import path

from core.views import RegistrationView

urlpatterns = [
    path('', RegistrationView.as_view(), name='registration'),
]
