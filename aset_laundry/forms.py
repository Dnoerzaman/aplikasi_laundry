from django import forms
from .models import Aset, TransaksiAset

class AsetForm(forms.ModelForm):
    class Meta:
        model = Aset
        fields = [
            'nama_barang', 'jumlah', 'satuan', 'merk', 
            'serial_number', 'tahun_pengadaan', 'keterangan', 'tanggal_input'
        ]
        widgets = {
            'nama_barang': forms.TextInput(attrs={'class': 'form-control'}),
            'jumlah': forms.NumberInput(attrs={'class': 'form-control'}),
            'satuan': forms.Select(attrs={'class': 'form-select'}),
            'merk': forms.TextInput(attrs={'class': 'form-control'}),
            'serial_number': forms.TextInput(attrs={'class': 'form-control'}),
            'tahun_pengadaan': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Contoh: 2024'}),
            'keterangan': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'tanggal_input': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class TransaksiAsetForm(forms.ModelForm):
    class Meta:
        model = TransaksiAset
        fields = ['aset', 'jenis_transaksi', 'jumlah', 'tanggal', 'keterangan']
        widgets = {
            'aset': forms.Select(attrs={'class': 'form-select'}),
            'jenis_transaksi': forms.Select(attrs={'class': 'form-select'}),
            'jumlah': forms.NumberInput(attrs={'class': 'form-control'}),
            'tanggal': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'keterangan': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
