
# Create your views here.
from django.views.generic import TemplateView



class indexView(TemplateView):
    template_name = "index.html"

