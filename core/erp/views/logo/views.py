from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import *

from core.erp.forms import logoForm
from core.erp.models import logo


class LogoListView(ListView):
    model = logo
    template_name = 'logo/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in logo.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de logos'
        context['create_url'] = reverse_lazy('erp:logo_create')
        context['list_url'] = reverse_lazy('erp:logo_list')
        context['entity'] = 'logos'
        return context


class LogoCreateView(CreateView):
    model = logo
    form_class = logoForm
    template_name = 'logo/create.html'
    success_url = reverse_lazy('erp:logo_list')



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación una logo'
        context['entity'] = 'logos'
        context['list_url'] = reverse_lazy('erp:logo_list')
        context['action'] = 'add'
        return context


class LogoUpdateView(UpdateView):
    model = logo
    form_class = logoForm
    template_name = 'logo/create.html'
    success_url = reverse_lazy('erp:logo_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición una logo'
        context['entity'] = 'logos'
        context['list_url'] = reverse_lazy('erp:logos_list')
        context['action'] = 'edit'
        return context


class LogoDeleteView(DeleteView):
    model = logo
    template_name = 'logo/delete.html'
    success_url = reverse_lazy('erp:logo_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de una Logo'
        context['entity'] = 'Logos'
        context['list_url'] = reverse_lazy('erp:logo_list')
        return context
