from django.urls import path

from core.views import RegistrationView, ConfirmRegistrationView

urlpatterns = [
    path("", RegistrationView.as_view(), name="registration"),
    path("confirm/", ConfirmRegistrationView.as_view(), name="confirm"),
]
