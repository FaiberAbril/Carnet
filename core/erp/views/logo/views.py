from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import *

from core.erp.forms import logoForm
from core.erp.models import logo
import os

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

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de un logo'
        context['entity'] = 'logos'
        context['list_url'] = reverse_lazy('erp:logo_list')
        context['action'] = 'add'
        return context


class LogoUpdateView(UpdateView):
    model = logo
    form_class = logoForm
    template_name = 'logo/create.html'
    success_url = reverse_lazy('erp:logo_list')

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición una logo'
        context['entity'] = 'logos'
        context['list_url'] = reverse_lazy('erp:logo_list')
        context['action'] = 'edit'
        return context


class LogoDeleteView(DeleteView):
    model = logo
    template_name = 'logo/delete.html'
    success_url = reverse_lazy('erp:logo_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        # Get the instance to be deleted
        self.object = self.get_object()
        
        # Delete the associated media file
        if self.object.logoimg:  # Assuming 'image' is the field name for the media file
            # Construct the path to the media file
            media_file_path = self.object.logoimg.path
            
            # Check if the media file exists before deleting
            if os.path.exists(media_file_path):
                # Delete the media file from the file system
                os.remove(media_file_path)
        
        # Call the parent delete method to delete the object from the database
        return super().delete(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de una Logo'
        context['entity'] = 'Logos'
        context['list_url'] = reverse_lazy('erp:logo_list')
        return context
