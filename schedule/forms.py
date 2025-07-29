from django import forms
from .models import Tugas

class TugasForm(forms.ModelForm):
    class Meta:
        model = Tugas
        fields = ['judul', 'deskripsi', 'status', 'penanggung_jawab', 'target_waktu', 'periode']
        widgets = {
            'judul': forms.TextInput(attrs={'class': 'form-control'}),
            'deskripsi': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'penanggung_jawab': forms.Select(attrs={'class': 'form-select'}),
            'target_waktu': forms.Select(attrs={'class': 'form-select'}),
            'periode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contoh: Juli 2025'}),
        }
