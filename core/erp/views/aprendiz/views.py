from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import *
from django.http import HttpResponseRedirect

from django.shortcuts import render
from django.http import HttpResponse

from core.erp.forms import AprendizForm
from core.erp.models import Aprendiz,logo


def generar_carnet_pdf(request,pk):
    datos = Aprendiz.objects.filter(pk=pk)
    imglogo = logo.objects.all()

    return render(request, 'aprendiz/generar.html',{'datos': datos,'imglogo': imglogo})


class AprendizListView(ListView):
    model = Aprendiz
    template_name = 'aprendiz/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Aprendiz.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        print(data)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Aprendices'
        context['create_url'] = reverse_lazy('erp:aprendiz_create')
        context['list_url'] = reverse_lazy('erp:aprendiz_list')
        context['entity'] = 'Aprendiz'
        return context

class AprendizCreateView(CreateView):
    model = Aprendiz
    form_class = AprendizForm
    template_name = 'aprendiz/create.html'
    success_url = reverse_lazy('erp:aprendiz_list')

    def form_valid(self, form):

        
        self.object = form.save()
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación una Aprendiz'
        context['entity'] = 'Aprendiz'
        context['list_url'] = reverse_lazy('erp:aprendiz_list')
        context['action'] = 'add'
        return context
    

class AprendizupdateView(UpdateView):
    model = Aprendiz
    form_class = AprendizForm
    template_name = 'aprendiz/create.html'
    success_url = reverse_lazy('erp:aprendiz_list')

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición una Aprendiz'
        context['entity'] = 'Aprendiz'
        context['list_url'] = reverse_lazy('erp:aprendiz_list')
        context['action'] = 'edit'
        return context


class AprendizDeleteView(DeleteView):
    model = Aprendiz
    template_name = 'aprendiz/delete.html'
    success_url = reverse_lazy('erp:aprendiz_list')

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
        context['title'] = 'Eliminación de una Aprendiz'
        context['entity'] = 'Centros'
        context['list_url'] = reverse_lazy('erp:aprendiz_list')
        return context


