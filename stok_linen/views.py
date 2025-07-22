from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.contrib import messages
from .models import StokLinen, TransaksiLinen
from .forms import StokLinenForm, TransaksiLinenForm

# --- Views untuk Stok Linen ---

class StokLinenListView(LoginRequiredMixin, ListView):
    model = StokLinen
    template_name = 'stok_linen/stoklinen_list.html'
    context_object_name = 'semua_stok_linen'
    paginate_by = 10

class StokLinenCreateView(LoginRequiredMixin, CreateView):
    model = StokLinen
    form_class = StokLinenForm
    template_name = 'stok_linen/stoklinen_form.html'
    success_url = reverse_lazy('stok_linen:stok-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Tambah Stok Linen Baru'
        return context

class StokLinenUpdateView(LoginRequiredMixin, UpdateView):
    model = StokLinen
    form_class = StokLinenForm
    template_name = 'stok_linen/stoklinen_form.html'
    success_url = reverse_lazy('stok_linen:stok-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ubah Stok Linen'
        return context

# --- Views untuk Transaksi Linen ---

class TransaksiLinenCreateView(LoginRequiredMixin, CreateView):
    model = TransaksiLinen
    form_class = TransaksiLinenForm
    template_name = 'stok_linen/transaksilinen_form.html'
    success_url = reverse_lazy('stok_linen:transaksi-catat')

    def get_context_data(self, **kwargs):
        """Menambahkan riwayat transaksi ke context."""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Catat Transaksi Linen'
        # Ambil 10 transaksi terakhir untuk ditampilkan sebagai riwayat
        context['riwayat_transaksi'] = TransaksiLinen.objects.all()[:10]
        return context

    def form_valid(self, form):
        try:
            with transaction.atomic():
                transaksi = form.save(commit=False)
                stok_item = transaksi.stok_linen

                if transaksi.jenis_transaksi == 'MASUK':
                    stok_item.stok_akhir += transaksi.jumlah
                elif transaksi.jenis_transaksi == 'KELUAR':
                    if stok_item.stok_akhir < transaksi.jumlah:
                        form.add_error('jumlah', f'Stok {stok_item.get_nama_linen_display()} di {stok_item.get_ruangan_display()} tidak mencukupi.')
                        return self.form_invalid(form)
                    stok_item.stok_akhir -= transaksi.jumlah
                
                stok_item.save()
                transaksi.petugas = self.request.user
                transaksi.save()
                messages.success(self.request, 'Transaksi linen berhasil dicatat dan stok telah diperbarui.')

        except Exception as e:
            messages.error(self.request, f"Terjadi kesalahan: {e}")
            return self.form_invalid(form)

        return super().form_valid(form)
