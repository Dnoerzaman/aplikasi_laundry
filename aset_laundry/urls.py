from django.urls import path
from .views import (
    AsetListView,
    AsetCreateView,
    AsetUpdateView,
    AsetDeleteView,
    TransaksiAsetCreateView,
)

app_name = 'aset_laundry'

urlpatterns = [
    path('', AsetListView.as_view(), name='aset-list'),
    path('tambah/', AsetCreateView.as_view(), name='aset-tambah'),
    path('ubah/<int:pk>/', AsetUpdateView.as_view(), name='aset-ubah'),
    path('hapus/<int:pk>/', AsetDeleteView.as_view(), name='aset-hapus'),
    path('transaksi/', TransaksiAsetCreateView.as_view(), name='transaksi-catat'),
]
