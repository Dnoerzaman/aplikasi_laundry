from django.urls import path
from .views import (
    StokChemicalListView, StokChemicalCreateView, StokChemicalUpdateView, StokChemicalDeleteView,
    PemakaianChemicalListView, PemakaianChemicalCreateView,
    PenerimaanChemicalListView, PenerimaanChemicalCreateView,
)

app_name = 'chemical'

urlpatterns = [
    # URLs untuk Stok Utama
    path('', StokChemicalListView.as_view(), name='stok-list'),
    path('tambah/', StokChemicalCreateView.as_view(), name='stok-tambah'),
    path('ubah/<int:pk>/', StokChemicalUpdateView.as_view(), name='stok-ubah'),
    path('hapus/<int:pk>/', StokChemicalDeleteView.as_view(), name='stok-hapus'),
    
    # URLs untuk Riwayat Pemakaian
    path('pemakaian/catat/', PemakaianChemicalCreateView.as_view(), name='pemakaian-catat'),
    path('pemakaian/', PemakaianChemicalListView.as_view(), name='pemakaian-list'),

    # URLs untuk Riwayat Penerimaan (Stok Masuk)
    path('penerimaan/', PenerimaanChemicalListView.as_view(), name='penerimaan-list'),
    path('penerimaan/tambah/', PenerimaanChemicalCreateView.as_view(), name='penerimaan-tambah'),
]
