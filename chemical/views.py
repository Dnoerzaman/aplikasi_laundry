from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.contrib import messages
from .models import StokChemical, PemakaianChemical
from .forms import StokChemicalForm, PemakaianChemicalForm

# --- Views untuk Stok Chemical (CRUD) ---

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

# --- Views untuk Pemakaian Chemical ---

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
        """
        Method ini dijalankan saat form pemakaian valid.
        Di sinilah logika pengurangan stok otomatis terjadi.
        """
        try:
            with transaction.atomic():
                # 1. Ambil data dari form tanpa menyimpan ke DB dulu
                pemakaian = form.save(commit=False)
                chemical = pemakaian.chemical

                # 2. Validasi: Cek apakah stok mencukupi
                if chemical.jumlah_stok < pemakaian.jumlah:
                    form.add_error('jumlah', f'Stok {chemical.nama_chemical} tidak mencukupi. Stok tersedia: {chemical.jumlah_stok} {chemical.unit}.')
                    return self.form_invalid(form)

                # 3. Kurangi stok
                chemical.jumlah_stok -= pemakaian.jumlah
                chemical.save()

                # 4. Simpan data pemakaian
                pemakaian.petugas = self.request.user
                pemakaian.save()
                
                messages.success(self.request, f"Pemakaian {chemical.nama_chemical} berhasil dicatat. Stok telah diperbarui.")
        except Exception as e:
            messages.error(self.request, f"Terjadi kesalahan: {e}")
            return self.form_invalid(form)
            
        return super().form_valid(form)
