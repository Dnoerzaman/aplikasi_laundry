from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import PenerimaanLinenForm, ItemLinenFormSet, BeratLinenHarianForm
from .models import BeratLinenHarian

@login_required
def checklist_penerimaan_view(request):
    title = "Form Checklist Penerimaan Linen"
    formset_prefix = 'items'

    if request.method == 'POST':
        penerimaan_form = PenerimaanLinenForm(request.POST)
        item_formset = ItemLinenFormSet(request.POST, prefix=formset_prefix)

        if penerimaan_form.is_valid() and item_formset.is_valid():
            try:
                with transaction.atomic():
                    penerimaan = penerimaan_form.save(commit=False)
                    penerimaan.petugas = request.user
                    penerimaan.save()
                    
                    item_formset.instance = penerimaan
                    item_formset.save()
                    
                    messages.success(request, 'Data penerimaan berhasil disimpan!')
                    return redirect('dashboard')
            except Exception as e:
                messages.error(request, f"Terjadi kesalahan saat menyimpan data: {e}")

    else:
        penerimaan_form = PenerimaanLinenForm()
        item_formset = ItemLinenFormSet(prefix=formset_prefix)

    context = {
        'title': title,
        'penerimaan_form': penerimaan_form,
        'item_formset': item_formset,
    }
    return render(request, 'checklist/checklist_form.html', context)

class BeratLinenListView(LoginRequiredMixin, ListView):
    model = BeratLinenHarian
    template_name = 'checklist/beratlinen_list.html'
    context_object_name = 'semua_data_berat'
    paginate_by = 10

class BeratLinenCreateView(LoginRequiredMixin, CreateView):
    model = BeratLinenHarian
    form_class = BeratLinenHarianForm
    template_name = 'checklist/beratlinen_form.html'
    success_url = reverse_lazy('checklist:berat-list')

    def form_valid(self, form):
        form.instance.petugas = self.request.user
        messages.success(self.request, 'Data berat linen berhasil ditambahkan.')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Tambah Catatan Berat Linen'
        return context

class BeratLinenUpdateView(LoginRequiredMixin, UpdateView):
    model = BeratLinenHarian
    form_class = BeratLinenHarianForm
    template_name = 'checklist/beratlinen_form.html'
    success_url = reverse_lazy('checklist:berat-list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Data berat linen berhasil diperbarui.')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ubah Catatan Berat Linen'
        return context

class BeratLinenDeleteView(LoginRequiredMixin, DeleteView):
    model = BeratLinenHarian
    template_name = 'checklist/beratlinen_confirm_delete.html'
    success_url = reverse_lazy('checklist:berat-list')

    def form_valid(self, form):
        messages.success(self.request, 'Data berat linen berhasil dihapus.')
        return super().form_valid(form)
