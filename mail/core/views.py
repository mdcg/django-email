from django.shortcuts import render
from django.views import View


class RegistrationView(View):
    def get(self, request):
        return render(request, "core/registration.html", {})

    def post(self, request):
        pass


class ConfirmRegistrationView(View):
    def get(self, request):
        pass