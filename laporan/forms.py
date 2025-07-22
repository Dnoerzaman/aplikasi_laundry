from django import forms

class ReportFilterForm(forms.Form):
    start_date = forms.DateField(
        label="Tanggal Mulai",
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    end_date = forms.DateField(
        label="Tanggal Selesai",
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
