from django.urls import path
from .views import (
        StokLinenListView,
        StokLinenCreateView,
        StokLinenUpdateView,
        TransaksiLinenCreateView,
)

app_name = 'stok_linen'

urlpatterns = [
        path('', StokLinenListView.as_view(), name='stok-list'),
        path('tambah/', StokLinenCreateView.as_view(), name='stok-tambah'),
        path('ubah/<int:pk>/', StokLinenUpdateView.as_view(), name='stok-ubah'),
        path('transaksi/', TransaksiLinenCreateView.as_view(), name='transaksi-catat'),
]
    