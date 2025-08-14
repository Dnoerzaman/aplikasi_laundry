from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Sum
from datetime import timedelta
import calendar

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

    # --- Pengambilan Data ---
    # 1. Penerimaan Linen (Total)
    penerimaan_bulan_ini = PenerimaanLinen.objects.filter(tanggal__range=[start_of_month, end_of_month]).count()

    # 2. Pemakaian Chemical (Total)
    pemakaian_chemical_bulan_ini = PemakaianChemical.objects.filter(tanggal__range=[start_of_month, end_of_month]).count()

    # 3. Rencana Kerja (Total)
    rencana_kerja_aktif = Tugas.objects.exclude(status='Selesai').count()

    # 4. Kalkulasi Berat Linen per Ruangan
    ruangan_choices = PenerimaanLinen.PilihanRuangan.choices
    
    # Ambil data agregat dari database
    berat_mingguan_qs = BeratLinenHarian.objects.filter(
        tanggal__range=[start_of_week, end_of_week]
    ).values('ruangan').annotate(total=Sum('total_berat'))
    
    berat_bulanan_qs = BeratLinenHarian.objects.filter(
        tanggal__range=[start_of_month, end_of_month]
    ).values('ruangan').annotate(total=Sum('total_berat'))

    # Ubah ke dictionary untuk pencarian cepat
    berat_mingguan_dict = {item['ruangan']: item['total'] for item in berat_mingguan_qs}
    berat_bulanan_dict = {item['ruangan']: item['total'] for item in berat_bulanan_qs}

    # Siapkan data untuk dikirim ke template
    data_berat_per_ruangan = []
    for value, label in ruangan_choices:
        data_berat_per_ruangan.append({
            'nama_ruangan': label,
            'berat_minggu_ini': berat_mingguan_dict.get(value, 0),
            'berat_bulan_ini': berat_bulanan_dict.get(value, 0)
        })

    context = {
        'penerimaan_bulan_ini': penerimaan_bulan_ini,
        'pemakaian_chemical_bulan_ini': pemakaian_chemical_bulan_ini,
        'rencana_kerja_aktif': rencana_kerja_aktif,
        'data_berat_per_ruangan': data_berat_per_ruangan,
    }
    return render(request, 'accounts/dashboard.html', context)