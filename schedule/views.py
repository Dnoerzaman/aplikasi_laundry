from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tugas
from .forms import TugasForm

class TugasListView(LoginRequiredMixin, ListView):
    model = Tugas
    template_name = 'schedule/tugas_list.html'
    context_object_name = 'semua_tugas'
    paginate_by = 10

class TugasCreateView(LoginRequiredMixin, CreateView):
    model = Tugas
    form_class = TugasForm
    template_name = 'schedule/tugas_form.html'
    success_url = reverse_lazy('schedule:tugas-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Tambah Rencana Kerja Baru'
        return context

class TugasUpdateView(LoginRequiredMixin, UpdateView):
    model = Tugas
    form_class = TugasForm
    template_name = 'schedule/tugas_form.html'
    success_url = reverse_lazy('schedule:tugas-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ubah Rencana Kerja'
        return context

class TugasDeleteView(LoginRequiredMixin, DeleteView):
    model = Tugas
    template_name = 'schedule/tugas_confirm_delete.html'
    success_url = reverse_lazy('schedule:tugas-list')
