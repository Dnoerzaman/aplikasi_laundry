from django.urls import path
from .views import (
    StokChemicalListView,
    StokChemicalCreateView,
    StokChemicalUpdateView,
    StokChemicalDeleteView,
    PemakaianChemicalListView,
    PemakaianChemicalCreateView,
)

app_name = 'chemical'

urlpatterns = [
    # URLs untuk Stok
    path('', StokChemicalListView.as_view(), name='stok-list'),
    path('tambah/', StokChemicalCreateView.as_view(), name='stok-tambah'),
    path('ubah/<int:pk>/', StokChemicalUpdateView.as_view(), name='stok-ubah'),
    path('hapus/<int:pk>/', StokChemicalDeleteView.as_view(), name='stok-hapus'),
    
    # URLs untuk Pemakaian
    path('pemakaian/catat/', PemakaianChemicalCreateView.as_view(), name='pemakaian-catat'), 
    path('pemakaian/', PemakaianChemicalListView.as_view(), name='pemakaian-list'),
]
