from django.urls import path
from core.erp.views.category.views import *
from core.erp.views.cargo.views import *
from core.erp.views.regional.views import *
from core.erp.views.centro.views import *
from core.erp.views.formacion.views import *
from core.erp.views.aprendiz.views import *
from core.erp.views.funcionario.views import *
from core.erp.views.logo.views import *

app_name = 'erp'

urlpatterns = [
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('cargo/list/', CargoListView.as_view(), name='cargo_list'),
    path('cargo/add/', CargoCreateView.as_view(), name='cargo_create'),
    path('cargo/update/<int:pk>/', CargoUpdateView.as_view(), name='cargo_update'),
    path('cargo/delete/<int:pk>/', CargoDeleteView.as_view(), name='cargo_delete'),
    path('regional/list/', regionalListView.as_view(), name='regional_list'),
    path('regional/add/', RegionalCreateView.as_view(), name='regional_create'),
    path('regional/update/<int:pk>/', RegionalUpdateView.as_view(), name='regional_update'),
    path('regional/delete/<int:pk>/', RegionalDeleteView.as_view(), name='regioanl_delete'),
    path('centro/list/', centroListView.as_view(), name='centro_list'),
    path('centro/add/', centroCreateView.as_view(), name='centro_create'),
    path('centro/update/<int:pk>/', centroUpdateView.as_view(), name='centro_update'),
    path('centro/delete/<int:pk>/', CentroDeleteView.as_view(), name='centro_delete'),
    path('formacion/list/', formacionListView.as_view(), name='formacion_list'),
    path('formacion/add/', formacionCreateView.as_view(), name='formacion_create'),
    path('formacion/update/<int:pk>/', formacionUpdateView.as_view(), name='formacion_update'),
    path('formacion/delete/<int:pk>/', formacionDeleteView.as_view(), name='formacion_delete'),
    path('aprendiz/list/', AprendizListView.as_view(), name='aprendiz_list'),
    path('aprendiz/add/', AprendizCreateView.as_view(), name='aprendiz_create'),
    path('aprendiz/update/<int:pk>/', AprendizupdateView.as_view(), name='aprendiz_update'),
    path('aprendiz/delete/<int:pk>/', AprendizDeleteView.as_view(), name='aprendiz_delete'),
    path('funcionario/list/', funcionarioListView.as_view(), name='funcionario_list'),
    path('funcionario/add/', funcionarioCreateView.as_view(), name='funcionario_create'),
    path('funcionario/update/<int:pk>/', funcionarioupdateView.as_view(), name='funcionario_update'),
    path('funcionario/delete/<int:pk>/', funcionarioDeleteView.as_view(), name='funcionario_delete'),
    path('logo/list/', LogoListView.as_view(), name='logo_list'),
    path('logo/add/', LogoCreateView.as_view(), name='logo_create'),
    path('logo/update/<int:pk>/', LogoUpdateView.as_view(), name='logo_update'),
    path('logo/delete/<int:pk>/', LogoDeleteView.as_view(), name='logo_delete'),
]
