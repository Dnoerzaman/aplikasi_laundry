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
    # 1. Penerimaan Linen
    penerimaan_minggu_ini = PenerimaanLinen.objects.filter(tanggal__range=[start_of_week, end_of_week]).count()
    penerimaan_bulan_ini = PenerimaanLinen.objects.filter(tanggal__range=[start_of_month, end_of_month]).count()

    # 2. Berat Linen Kotor
    berat_minggu_ini = BeratLinenHarian.objects.filter(tanggal__range=[start_of_week, end_of_week]).aggregate(total=Sum('total_berat'))['total'] or 0
    berat_bulan_ini = BeratLinenHarian.objects.filter(tanggal__range=[start_of_month, end_of_month]).aggregate(total=Sum('total_berat'))['total'] or 0

    # 3. Pemakaian Chemical
    pemakaian_chemical_bulan_ini = PemakaianChemical.objects.filter(tanggal__range=[start_of_month, end_of_month]).count()

    # 4. Rencana Kerja
    rencana_kerja_aktif = Tugas.objects.exclude(status='Selesai').count()

    context = {
        'penerimaan_minggu_ini': penerimaan_minggu_ini,
        'penerimaan_bulan_ini': penerimaan_bulan_ini,
        'berat_minggu_ini': berat_minggu_ini,
        'berat_bulan_ini': berat_bulan_ini,
        'pemakaian_chemical_bulan_ini': pemakaian_chemical_bulan_ini,
        'rencana_kerja_aktif': rencana_kerja_aktif,
    }
    return render(request, 'accounts/dashboard.html', context)
