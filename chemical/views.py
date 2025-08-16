from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.contrib import messages
from .models import StokChemical, PemakaianChemical, PenerimaanChemical
from .forms import StokChemicalForm, PemakaianChemicalForm, PenerimaanChemicalForm

class StokChemicalListView(LoginRequiredMixin, ListView):
    model = StokChemical
    template_name = 'chemical/stokchemical_list.html'
    context_object_name = 'semua_stok'
    paginate_by = 10

class StokChemicalCreateView(LoginRequiredMixin, CreateView):
    model = StokChemical
    form_class = StokChemicalForm
    template_name = 'chemical/stokchemical_form.html'
    success_url = reverse_lazy('chemical:stok-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Tambah Chemical Baru'
        return context

class StokChemicalUpdateView(LoginRequiredMixin, UpdateView):
    model = StokChemical
    form_class = StokChemicalForm
    template_name = 'chemical/stokchemical_form.html'
    success_url = reverse_lazy('chemical:stok-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ubah Stok Chemical'
        return context

class StokChemicalDeleteView(LoginRequiredMixin, DeleteView):
    model = StokChemical
    template_name = 'chemical/stokchemical_confirm_delete.html'
    success_url = reverse_lazy('chemical:stok-list')

class PemakaianChemicalListView(LoginRequiredMixin, ListView):
    model = PemakaianChemical
    template_name = 'chemical/pemakaianchemical_list.html'
    context_object_name = 'semua_pemakaian'
    paginate_by = 10

class PemakaianChemicalCreateView(LoginRequiredMixin, CreateView):
    model = PemakaianChemical
    form_class = PemakaianChemicalForm
    template_name = 'chemical/pemakaianchemical_form.html'
    success_url = reverse_lazy('chemical:pemakaian-list')

    def form_valid(self, form):
        try:
            with transaction.atomic():
                pemakaian = form.save(commit=False)
                chemical = pemakaian.chemical

                if chemical.jumlah_stok < pemakaian.jumlah:
                    form.add_error('jumlah', f'Stok {chemical.nama_chemical} tidak mencukupi. Stok tersedia: {chemical.jumlah_stok} {chemical.unit}.')
                    return self.form_invalid(form)

                chemical.jumlah_stok -= pemakaian.jumlah
                chemical.save()

                pemakaian.petugas = self.request.user
                pemakaian.save()
                
                messages.success(self.request, f"Pemakaian {chemical.nama_chemical} berhasil dicatat. Stok telah diperbarui.")
        except Exception as e:
            messages.error(self.request, f"Terjadi kesalahan: {e}")
            return self.form_invalid(form)
            
        return super().form_valid(form)

class PenerimaanChemicalListView(LoginRequiredMixin, ListView):
    model = PenerimaanChemical
    template_name = 'chemical/penerimaanchemical_list.html'
    context_object_name = 'semua_penerimaan'
    paginate_by = 10

class PenerimaanChemicalCreateView(LoginRequiredMixin, CreateView):
    model = PenerimaanChemical
    form_class = PenerimaanChemicalForm
    template_name = 'chemical/penerimaanchemical_form.html'
    success_url = reverse_lazy('chemical:penerimaan-list')

    def form_valid(self, form):
        try:
            with transaction.atomic():
                penerimaan = form.save(commit=False)
                stok_item = penerimaan.chemical

                # Logika utama: tambahkan stok
                stok_item.jumlah_stok += penerimaan.jumlah
                stok_item.save()

                # Simpan data transaksi penerimaan
                penerimaan.petugas = self.request.user
                penerimaan.save()
                
                messages.success(self.request, f"Stok {stok_item.nama_chemical} berhasil ditambahkan.")
        except Exception as e:
            messages.error(self.request, f"Terjadi kesalahan: {e}")
            return self.form_invalid(form)
            
        return super().form_valid(form)
