from django.urls import path
from .views import (
    ReportDashboardView,
    ExportChecklistExcel,
    ExportPemakaianChemicalExcel,
    ExportTransaksiLinenExcel,
    ExportAsetExcel,
    ExportScheduleExcel,
    ExportStokChemicalExcel,
    ExportBeratLinenExcel,
)

app_name = 'laporan'

urlpatterns = [
    path('', ReportDashboardView.as_view(), name='report-dashboard'),
    path('export/checklist/', ExportChecklistExcel.as_view(), name='export-checklist'),
    path('export/pemakaian-chemical/', ExportPemakaianChemicalExcel.as_view(), name='export-pemakaian-chemical'),
    path('export/transaksi-linen/', ExportTransaksiLinenExcel.as_view(), name='export-transaksi-linen'),
    path('export/berat-linen/', ExportBeratLinenExcel.as_view(), name='export-berat-linen'),
    path('export/aset/', ExportAsetExcel.as_view(), name='export-aset'),
    path('export/schedule/', ExportScheduleExcel.as_view(), name='export-schedule'),
    path('export/stok-chemical/', ExportStokChemicalExcel.as_view(), name='export-stok-chemical'),
]
