from django.db import models
from django.conf import settings
from django.utils import timezone

class StokChemical(models.Model):
    class PilihanNama(models.TextChoices):
        ALKALI = 'Alkali', 'Alkali'
        EMULSIFIER = 'Emulsifier', 'Emulsifier'
        OXYGEN = 'Oxygen', 'Oxygen'
        SOFTENER = 'Softener', 'Softener'
        PELICIN = 'Pelicin', 'Pelicin'
        LAINNYA = 'Chemical Lainnya', 'Chemical Lainnya'

    class PilihanUnit(models.TextChoices):
        LITER = 'Liter', 'Liter'
        KILOGRAM = 'Kg', 'Kilogram'
        PCS = 'Pcs', 'Pcs'

    nama_chemical = models.CharField(
        max_length=100,
        choices=PilihanNama.choices,
        unique=True,
        verbose_name="Nama Chemical"
    )
    jumlah_stok = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, verbose_name="Jumlah Stok")
    unit = models.CharField(max_length=10, choices=PilihanUnit.choices, verbose_name="Satuan")
    dibuat_pada = models.DateTimeField(auto_now_add=True, verbose_name="Tanggal Input")
    update_terakhir = models.DateTimeField(auto_now=True, verbose_name="Update Terakhir")

    def __str__(self):
        return self.get_nama_chemical_display()

    class Meta:
        verbose_name = "Stok Chemical"
        verbose_name_plural = "Daftar Stok Chemical"
        ordering = ['nama_chemical']

class PemakaianChemical(models.Model):
    chemical = models.ForeignKey(StokChemical, on_delete=models.PROTECT, related_name='pemakaian', verbose_name="Chemical yang Digunakan")
    tanggal = models.DateField(verbose_name="Tanggal Pemakaian")
    jumlah = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Jumlah Pemakaian")
    petugas = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name="Petugas")
    keterangan = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Pemakaian {self.chemical.nama_chemical} sebanyak {self.jumlah} {self.chemical.unit}"

    class Meta:
        verbose_name = "Pemakaian Chemical"
        verbose_name_plural = "Riwayat Pemakaian Chemical"
        ordering = ['-tanggal']


class PenerimaanChemical(models.Model):
    """
    Model untuk mencatat setiap transaksi stok chemical yang masuk.
    """
    chemical = models.ForeignKey(StokChemical, on_delete=models.PROTECT, related_name='penerimaan', verbose_name="Chemical yang Diterima")
    jumlah = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Jumlah Masuk")
    tanggal = models.DateField(verbose_name="Tanggal Penerimaan")
    petugas = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name="Petugas")
    keterangan = models.TextField(blank=True, null=True, verbose_name="Keterangan (Contoh: No. Faktur)")

    def __str__(self):
        return f"Penerimaan {self.chemical.nama_chemical} sebanyak {self.jumlah} {self.chemical.unit}"

    class Meta:
        verbose_name = "Penerimaan Chemical"
        verbose_name_plural = "Riwayat Penerimaan Chemical"
        ordering = ['-tanggal']
