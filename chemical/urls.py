from django.urls import path
from .views import (
<<<<<<< HEAD
    StokChemicalListView, StokChemicalCreateView, StokChemicalUpdateView, StokChemicalDeleteView,
    PemakaianChemicalListView, PemakaianChemicalCreateView,
    PenerimaanChemicalListView, PenerimaanChemicalCreateView,
=======
    StokChemicalListView,
    StokChemicalCreateView,
    StokChemicalUpdateView,
    StokChemicalDeleteView,
    PemakaianChemicalListView,
    PemakaianChemicalCreateView,
>>>>>>> e6bd4a31ed08b1db63967fbd062834b409247b88
)

app_name = 'chemical'

urlpatterns = [
<<<<<<< HEAD
    # URLs untuk Stok Utama
=======
    # URLs untuk Stok
>>>>>>> e6bd4a31ed08b1db63967fbd062834b409247b88
    path('', StokChemicalListView.as_view(), name='stok-list'),
    path('tambah/', StokChemicalCreateView.as_view(), name='stok-tambah'),
    path('ubah/<int:pk>/', StokChemicalUpdateView.as_view(), name='stok-ubah'),
    path('hapus/<int:pk>/', StokChemicalDeleteView.as_view(), name='stok-hapus'),
    
<<<<<<< HEAD
    # URLs untuk Riwayat Pemakaian
    path('pemakaian/catat/', PemakaianChemicalCreateView.as_view(), name='pemakaian-catat'),
    path('pemakaian/', PemakaianChemicalListView.as_view(), name='pemakaian-list'),

    # URLs untuk Riwayat Penerimaan (Stok Masuk)
    path('penerimaan/', PenerimaanChemicalListView.as_view(), name='penerimaan-list'),
    path('penerimaan/tambah/', PenerimaanChemicalCreateView.as_view(), name='penerimaan-tambah'),
=======
    # URLs untuk Pemakaian
    path('pemakaian/catat/', PemakaianChemicalCreateView.as_view(), name='pemakaian-catat'), 
    path('pemakaian/', PemakaianChemicalListView.as_view(), name='pemakaian-list'),
>>>>>>> e6bd4a31ed08b1db63967fbd062834b409247b88
]
