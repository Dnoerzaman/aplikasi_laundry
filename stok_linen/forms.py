from django import forms
from .models import StokLinen, TransaksiLinen

class StokLinenForm(forms.ModelForm):
    class Meta:
        model = StokLinen
        fields = ['ruangan', 'nama_linen', 'stok_akhir', 'keterangan']
        widgets = {            
            'ruangan': forms.Select(attrs={'class': 'form-select'}),
            'nama_linen': forms.Select(attrs={'class': 'form-select'}),
            'stok_akhir': forms.NumberInput(attrs={'class': 'form-control'}),
            'keterangan': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class TransaksiLinenForm(forms.ModelForm):
    class Meta:
        model = TransaksiLinen
        fields = ['stok_linen', 'jenis_transaksi', 'jumlah', 'tanggal', 'keterangan']
        widgets = {
            'stok_linen': forms.Select(attrs={'class': 'form-select'}),
            'jenis_transaksi': forms.Select(attrs={'class': 'form-select'}),
            'jumlah': forms.NumberInput(attrs={'class': 'form-control'}),
            'tanggal': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'keterangan': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
