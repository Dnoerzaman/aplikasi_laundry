from django.urls import path
from .views import (
    checklist_penerimaan_view,
    BeratLinenListView,
    BeratLinenCreateView,
    BeratLinenUpdateView,
    BeratLinenDeleteView,
)

app_name = 'checklist'

urlpatterns = [
    path('tambah/', checklist_penerimaan_view, name='tambah_checklist'),
    # URLS untuk Berat Linen
    path('berat/', BeratLinenListView.as_view(), name='berat-list'),
    path('berat/tambah/', BeratLinenCreateView.as_view(), name='berat-tambah'),
    path('berat/ubah/<int:pk>/', BeratLinenUpdateView.as_view(), name='berat-ubah'),
    path('berat/hapus/<int:pk>/', BeratLinenDeleteView.as_view(), name='berat-hapus'),
]
