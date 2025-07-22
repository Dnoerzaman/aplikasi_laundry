from django import forms
from .models import StokChemical, PemakaianChemical

class StokChemicalForm(forms.ModelForm):
    class Meta:
        model = StokChemical
        fields = ['nama_chemical', 'jumlah_stok', 'unit']
        widgets = {
            'nama_chemical': forms.Select(attrs={'class': 'form-select'}),
            'jumlah_stok': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'unit': forms.Select(attrs={'class': 'form-select'}),
        }

class PemakaianChemicalForm(forms.ModelForm):
    class Meta:
        model = PemakaianChemical
        fields = ['tanggal', 'chemical', 'jumlah', 'keterangan']
        widgets = {
            'tanggal': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'chemical': forms.Select(attrs={'class': 'form-select'}),
            'jumlah': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'keterangan': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
  