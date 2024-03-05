from django.urls import path
from core.erp.views.category.views import *
from core.erp.views.cargo.views import *
from core.erp.views.regional.views import *


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
]
