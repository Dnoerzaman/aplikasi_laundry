from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Sum
from datetime import timedelta
import calendar
import json

# Import model dari aplikasi lain
from checklist.models import PenerimaanLinen, BeratLinenHarian
from chemical.models import PemakaianChemical
from schedule.models import Tugas

@login_required
def dashboard_view(request):
    today = timezone.now().date()

    # --- Kalkulasi Rentang Waktu ---
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=5)
    start_of_month = today.replace(day=1)
    _, num_days = calendar.monthrange(today.year, today.month)
    end_of_month = today.replace(day=num_days)

    # --- Pengambilan Data Agregat ---
    penerimaan_bulan_ini = PenerimaanLinen.objects.filter(tanggal__range=[start_of_month, end_of_month]).count()
    pemakaian_chemical_bulan_ini = PemakaianChemical.objects.filter(tanggal__range=[start_of_month, end_of_month]).count()
    rencana_kerja_aktif = Tugas.objects.exclude(status='Selesai').count()

    # --- Kalkulasi Berat Linen per Ruangan ---
    ruangan_choices = PenerimaanLinen.PilihanRuangan.choices
    
    berat_mingguan_qs = BeratLinenHarian.objects.filter(tanggal__range=[start_of_week, end_of_week]).values('ruangan').annotate(total=Sum('total_berat'))
    berat_bulanan_qs = BeratLinenHarian.objects.filter(tanggal__range=[start_of_month, end_of_month]).values('ruangan').annotate(total=Sum('total_berat'))

    berat_mingguan_dict = {item['ruangan']: item['total'] for item in berat_mingguan_qs}
    berat_bulanan_dict = {item['ruangan']: item['total'] for item in berat_bulanan_qs}

    data_berat_per_ruangan = []
    chart_labels = []
    chart_data = []

    for value, label in ruangan_choices:
        berat_bulan_ini = berat_bulanan_dict.get(value, 0)
        data_berat_per_ruangan.append({
            'nama_ruangan': label,
            'berat_minggu_ini': berat_mingguan_dict.get(value, 0),
            'berat_bulan_ini': berat_bulan_ini
        })
        # Siapkan data untuk chart hanya jika ada beratnya
        if berat_bulan_ini > 0:
            chart_labels.append(label)
            chart_data.append(float(berat_bulan_ini)) # Pastikan data dalam format float

    context = {
        'penerimaan_bulan_ini': penerimaan_bulan_ini,
        'pemakaian_chemical_bulan_ini': pemakaian_chemical_bulan_ini,
        'rencana_kerja_aktif': rencana_kerja_aktif,
        'data_berat_per_ruangan': data_berat_per_ruangan,
        # Mengirim data chart sebagai JSON string yang aman
        'chart_labels': json.dumps(chart_labels),
        'chart_data': json.dumps(chart_data),
    }
    return render(request, 'accounts/dashboard.html', context)
