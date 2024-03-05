from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import *

from core.erp.forms import CentroForm
from core.erp.models import Centro


class centroListView(ListView):
    model = Centro
    template_name = 'centro/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Centro.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Centro'
        context['create_url'] = reverse_lazy('erp:centro_create')
        context['list_url'] = reverse_lazy('erp:centro_list')
        context['entity'] = 'Centro'
        return context

class centroCreateView(CreateView):
    model = Centro
    form_class = CentroForm
    template_name = 'centro/create.html'
    success_url = reverse_lazy('erp:centro_list')

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
        context['title'] = 'Creación una Centro'
        context['entity'] = 'Centro'
        context['list_url'] = reverse_lazy('erp:centro_list')
        context['action'] = 'add'
        return context
    

class centroUpdateView(UpdateView):
    model = Centro
    form_class = CentroForm
    template_name = 'centro/create.html'
    success_url = reverse_lazy('erp:centro_list')

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
        context['title'] = 'Edición una Centro'
        context['entity'] = 'Centro'
        context['list_url'] = reverse_lazy('erp:centro_list')
        context['action'] = 'edit'
        return context


class CentroDeleteView(DeleteView):
    model = Centro
    template_name = 'centro/delete.html'
    success_url = reverse_lazy('erp:centro_list')

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
        context['title'] = 'Eliminación de una Centro'
        context['entity'] = 'Centros'
        context['list_url'] = reverse_lazy('erp:centro_list')
        return context
