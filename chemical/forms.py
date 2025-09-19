from django import forms
<<<<<<< HEAD
from .models import StokChemical, PemakaianChemical, PenerimaanChemical
=======
from .models import StokChemical, PemakaianChemical
>>>>>>> e6bd4a31ed08b1db63967fbd062834b409247b88

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
<<<<<<< HEAD

class PenerimaanChemicalForm(forms.ModelForm):
    class Meta:
        model = PenerimaanChemical
        fields = ['tanggal', 'chemical', 'jumlah', 'keterangan']
        widgets = {
            'tanggal': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'chemical': forms.Select(attrs={'class': 'form-select'}),
            'jumlah': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'keterangan': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
=======
>>>>>>> e6bd4a31ed08b1db63967fbd062834b409247b88
  