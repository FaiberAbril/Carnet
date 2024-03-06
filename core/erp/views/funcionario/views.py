from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import *

from core.erp.forms import funcionarioForm
from core.erp.models import funcionario


class funcionarioListView(ListView):
    model = funcionario
    template_name = 'funcionario/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in funcionario.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        print(data)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de funcionarios'
        context['create_url'] = reverse_lazy('erp:funcionario_create')
        context['list_url'] = reverse_lazy('erp:funcionario_list')
        context['entity'] = 'Funcionario'
        return context

class funcionarioCreateView(CreateView):
    model = funcionario
    form_class = funcionarioForm
    template_name = 'funcionario/create.html'
    success_url = reverse_lazy('erp:funcionario_list')

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
        context['title'] = 'Creación una Funcionario'
        context['entity'] = 'Funcionario'
        context['list_url'] = reverse_lazy('erp:funcionario_list')
        context['action'] = 'add'
        return context
    

class funcionarioupdateView(UpdateView):
    model = funcionario
    form_class = funcionarioForm
    template_name = 'aprendiz/create.html'
    success_url = reverse_lazy('erp:aprendiz_list')

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
        context['title'] = 'Edición una funcionario'
        context['entity'] = 'funcionario'
        context['list_url'] = reverse_lazy('erp:funcionario_list')
        context['action'] = 'edit'
        return context


class funcionarioDeleteView(DeleteView):
    model = funcionario
    template_name = 'funcionario/delete.html'
    success_url = reverse_lazy('erp:funcionario_list')

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
        context['title'] = 'Eliminación de una funcionario'
        context['entity'] = 'funcionario'
        context['list_url'] = reverse_lazy('erp:funcionario_list')
        return context
