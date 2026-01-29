# project_laundry/urls.py
from django.contrib import admin
from django.urls import path, include
from accounts.views import dashboard_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('checklist/', include('checklist.urls')),
    path('stok/', include('chemical.urls')),
    path('stok-linen/', include('stok_linen.urls')),
    path('aset/', include('aset_laundry.urls')),
    path('log-pekerjaan/', include('log_pekerjaan.urls')),
    path('schedule/', include('schedule.urls')),
    path('laporan/', include('laporan.urls')),
    path('', dashboard_view, name='dashboard'),
]
