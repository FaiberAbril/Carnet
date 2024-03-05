from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import *

from core.erp.forms import RegionalForm
from core.erp.models import Regional


class regionalListView(ListView):
    model = Regional
    template_name = 'regional/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Regional.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Regionales'
        context['create_url'] = reverse_lazy('erp:regional_create')
        context['list_url'] = reverse_lazy('erp:regional_list')
        context['entity'] = 'Regionales'
        return context

class RegionalCreateView(CreateView):
    model = Regional
    form_class = RegionalForm
    template_name = 'regional/create.html'
    success_url = reverse_lazy('erp:regional_list')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación una Regional'
        context['entity'] = 'Regional'
        context['list_url'] = reverse_lazy('erp:regional_list')
        context['action'] = 'add'
        return context
    

class RegionalUpdateView(UpdateView):
    model = Regional
    form_class = RegionalForm
    template_name = 'regional/create.html'
    success_url = reverse_lazy('erp:regional_list')

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
        context['title'] = 'Edición una Regional'
        context['entity'] = 'Regional'
        context['list_url'] = reverse_lazy('erp:regional_list')
        context['action'] = 'edit'
        return context


class RegionalDeleteView(DeleteView):
    model = Regional
    template_name = 'regional/delete.html'
    success_url = reverse_lazy('erp:regional_list')

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
        context['title'] = 'Eliminación de una Regional'
        context['entity'] = 'Regionales'
        context['list_url'] = reverse_lazy('erp:regional_list')
        return context
