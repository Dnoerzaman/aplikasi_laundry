from django.urls import path
from .views import (
    TugasListView,
    TugasCreateView,
    TugasUpdateView,
    TugasDeleteView,
)

app_name = 'schedule'

urlpatterns = [
    path('', TugasListView.as_view(), name='tugas-list'),
    path('tambah/', TugasCreateView.as_view(), name='tugas-tambah'),
    path('ubah/<int:pk>/', TugasUpdateView.as_view(), name='tugas-ubah'),
    path('hapus/<int:pk>/', TugasDeleteView.as_view(), name='tugas-hapus'),
]