from django.urls import reverse_lazy
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.contrib import messages
from .models import Aset, TransaksiAset
from .forms import AsetForm, TransaksiAsetForm

class AsetListView(LoginRequiredMixin, ListView):
    model = Aset
    template_name = 'aset_laundry/aset_list.html'
    context_object_name = 'semua_aset'
    paginate_by = 10

class AsetCreateView(LoginRequiredMixin, CreateView):
    model = Aset
    form_class = AsetForm
    template_name = 'aset_laundry/aset_form.html'
    success_url = reverse_lazy('aset_laundry:aset-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Tambah Aset Baru'
        return context

class AsetUpdateView(LoginRequiredMixin, UpdateView):
    model = Aset
    form_class = AsetForm
    template_name = 'aset_laundry/aset_form.html'
    success_url = reverse_lazy('aset_laundry:aset-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ubah Data Aset'
        return context

class AsetDeleteView(LoginRequiredMixin, DeleteView):
    model = Aset
    template_name = 'aset_laundry/aset_confirm_delete.html'
    success_url = '/aset/'

    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, "Aset ini tidak bisa dihapus karena sudah memiliki riwayat transaksi. Hapus riwayat transaksinya terlebih dahulu.")
            return redirect('aset_laundry:aset-list')

class TransaksiAsetCreateView(LoginRequiredMixin, CreateView):
    model = TransaksiAset
    form_class = TransaksiAsetForm
    template_name = 'aset_laundry/transaksi_aset_form.html'
    success_url = reverse_lazy('aset_laundry:transaksi-catat')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Catat Transaksi Aset'
        context['riwayat_transaksi'] = TransaksiAset.objects.all()[:10]
        return context

    def form_valid(self, form):
        try:
            with transaction.atomic():
                transaksi = form.save(commit=False)
                aset_item = transaksi.aset

                if transaksi.jenis_transaksi == 'PENAMBAHAN':
                    aset_item.jumlah += transaksi.jumlah
                elif transaksi.jenis_transaksi == 'PENGURANGAN':
                    if aset_item.jumlah < transaksi.jumlah:
                        form.add_error('jumlah', f'Jumlah aset "{aset_item.nama_barang}" tidak mencukupi untuk dikurangi.')
                        return self.form_invalid(form)
                    aset_item.jumlah -= transaksi.jumlah
                
                aset_item.save()
                transaksi.petugas = self.request.user
                transaksi.save()
                messages.success(self.request, 'Transaksi aset berhasil dicatat dan jumlah aset telah diperbarui.')

        except Exception as e:
            messages.error(self.request, f"Terjadi kesalahan: {e}")
            return self.form_invalid(form)

        return super().form_valid(form)
