from django import forms
from .models import PenerimaanLinen, ItemLinen, BeratLinenHarian

class PenerimaanLinenForm(forms.ModelForm):
    class Meta:
        model = PenerimaanLinen
        fields = ['tanggal', 'jam', 'ruangan']
        widgets = {
            'tanggal': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'jam': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'ruangan': forms.Select(attrs={'class': 'form-select'}),
        }

class ItemLinenForm(forms.ModelForm):
    class Meta:
        model = ItemLinen
        fields = ['nama_item', 'jumlah', 'kondisi', 'keterangan']
        widgets = {
            'nama_item': forms.Select(attrs={'class': 'form-select'}),
            'jumlah': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'kondisi': forms.Select(attrs={'class': 'form-select'}),
            'keterangan': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Opsional'}),
        }

ItemLinenFormSet = forms.inlineformset_factory(
    PenerimaanLinen,
    ItemLinen,
    form=ItemLinenForm,
    extra=1,
    can_delete=True,
    min_num=1,
    validate_min=True,
)

class BeratLinenHarianForm(forms.ModelForm):
    class Meta:
        model = BeratLinenHarian
        fields = ['tanggal', 'ruangan', 'shift', 'total_berat']
        widgets = {
            'tanggal': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'ruangan': forms.Select(attrs={'class': 'form-select'}),
            'shift': forms.Select(attrs={'class': 'form-select'}),
            'total_berat': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Contoh: 15.5', 'step': '0.1'}),
        }
