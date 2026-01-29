from django import forms
from .models import LogPekerjaan

class LogPekerjaanForm(forms.ModelForm):
    class Meta:
        model = LogPekerjaan
        fields = ['tanggal', 'keterangan']
        widgets = {
            'tanggal': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
            'keterangan': forms.Textarea(
                attrs={
                    'class': 'form-control', 
                    'rows': 4, 
                    'placeholder': 'Tuliskan catatan pekerjaan atau kejadian penting di sini...'
                }
            ),
        }