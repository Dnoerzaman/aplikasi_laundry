from django.urls import path
from .views import (
    LogPekerjaanListView,
    LogPekerjaanCreateView,
    LogPekerjaanUpdateView,
    LogPekerjaanDeleteView,
)

app_name = 'log_pekerjaan'

urlpatterns = [
    path('', LogPekerjaanListView.as_view(), name='log-list'),
    path('tambah/', LogPekerjaanCreateView.as_view(), name='log-tambah'),
    path('ubah/<int:pk>/', LogPekerjaanUpdateView.as_view(), name='log-ubah'),
    path('hapus/<int:pk>/', LogPekerjaanDeleteView.as_view(), name='log-hapus'),
]