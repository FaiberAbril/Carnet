from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import *

from core.erp.forms import CargoForm
from core.erp.models import Cargo

class CargoListView(ListView):
    model = Cargo
    template_name = 'cargo/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Cargo.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Cargos'
        context['create_url'] = reverse_lazy('erp:cargo_create')
        context['list_url'] = reverse_lazy('erp:cargo_list')
        context['entity'] = 'Cargos'
        return context

class CargoCreateView(CreateView):
    model = Cargo
    form_class = CargoForm
    template_name = 'cargo/create.html'
    success_url = reverse_lazy('erp:cargo_list')

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
        context['title'] = 'Creación una Cargo'
        context['entity'] = 'Cargo'
        context['list_url'] = reverse_lazy('erp:cargo_list')
        context['action'] = 'add'
        return context
    

class CargoUpdateView(UpdateView):
    model = Cargo
    form_class = CargoForm
    template_name = 'cargo/create.html'
    success_url = reverse_lazy('erp:cargo_list')

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
        context['title'] = 'Edición una Cargo'
        context['entity'] = 'Cargo'
        context['list_url'] = reverse_lazy('erp:cargo_list')
        context['action'] = 'edit'
        return context


class CargoDeleteView(DeleteView):
    model = Cargo
    template_name = 'cargo/delete.html'
    success_url = reverse_lazy('erp:cargo_list')

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
        context['title'] = 'Eliminación de una Cargo'
        context['entity'] = 'Cargos'
        context['list_url'] = reverse_lazy('erp:cargo_list')
        return context
