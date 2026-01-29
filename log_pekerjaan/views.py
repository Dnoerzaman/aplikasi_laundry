from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import LogPekerjaan
from .forms import LogPekerjaanForm

class LogPekerjaanListView(LoginRequiredMixin, ListView):
    model = LogPekerjaan
    template_name = 'log_pekerjaan/logpekerjaan_list.html'
    context_object_name = 'semua_log'
    paginate_by = 10

class LogPekerjaanCreateView(LoginRequiredMixin, CreateView):
    model = LogPekerjaan
    form_class = LogPekerjaanForm
    template_name = 'log_pekerjaan/logpekerjaan_form.html'
    success_url = reverse_lazy('log_pekerjaan:log-list')

    def form_valid(self, form):
        # Mengisi kolom PJ secara otomatis dengan user yang sedang login
        form.instance.pj = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Tambah Log Pekerjaan"
        return context

class LogPekerjaanUpdateView(LoginRequiredMixin, UpdateView):
    model = LogPekerjaan
    form_class = LogPekerjaanForm
    template_name = 'log_pekerjaan/logpekerjaan_form.html'
    success_url = reverse_lazy('log_pekerjaan:log-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Ubah Log Pekerjaan"
        return context

class LogPekerjaanDeleteView(LoginRequiredMixin, DeleteView):
    model = LogPekerjaan
    template_name = 'log_pekerjaan/logpekerjaan_confirm_delete.html'
    success_url = reverse_lazy('log_pekerjaan:log-list')