from typing import Any
from django.contrib.auth.views import LoginView,LogoutView
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import redirect




class loginFormView(LoginView):
    template_name = "login.html"


    def dispatch(self, request, *args, **kwargs) :
        if request.user.is_authenticated:
            return redirect('erp:category_list')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar sesion'
        return context

class logoutFormView(LogoutView):
    pass