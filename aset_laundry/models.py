from django.db import models
from django.utils import timezone
from django.conf import settings

class Aset(models.Model):
    """
    Model untuk menyimpan data inventaris aset tetap di unit laundry.
    """
    class PilihanSatuan(models.TextChoices):
        UNIT = 'Unit', 'Unit'
        PCS = 'Pcs', 'Pcs'
        SET = 'Set', 'Set'
        BUAH = 'Buah', 'Buah'

    nama_barang = models.CharField(max_length=200, verbose_name="Nama Barang")
    jumlah = models.PositiveIntegerField(default=1, verbose_name="Jumlah")
    satuan = models.CharField(max_length=10, choices=PilihanSatuan.choices, default=PilihanSatuan.UNIT)
    merk = models.CharField(max_length=100, blank=True, null=True, verbose_name="Merk/Tipe")
    serial_number = models.CharField(max_length=100, blank=True, null=True, verbose_name="Serial Number (SN)")
    tahun_pengadaan = models.PositiveIntegerField(blank=True, null=True, verbose_name="Tahun Pengadaan")
    keterangan = models.TextField(blank=True, null=True)
    tanggal_input = models.DateField(default=timezone.now, verbose_name="Tanggal Input")

    def __str__(self):
        return self.nama_barang

    class Meta:
        verbose_name = "Aset"
        verbose_name_plural = "Daftar Aset"
        ordering = ['nama_barang']

class TransaksiAset(models.Model):
    """
    Model untuk mencatat setiap transaksi aset (penambahan atau pengurangan).
    """
    class PilihanTransaksi(models.TextChoices):
        PENAMBAHAN = 'PENAMBAHAN', 'Penambahan'
        PENGURANGAN = 'PENGURANGAN', 'Pengurangan'

    aset = models.ForeignKey(Aset, on_delete=models.PROTECT, related_name='transaksi', verbose_name="Aset")
    jenis_transaksi = models.CharField(max_length=20, choices=PilihanTransaksi.choices, verbose_name="Jenis Transaksi")
    jumlah = models.PositiveIntegerField()
    tanggal = models.DateField(default=timezone.now, verbose_name="Tanggal Transaksi")
    petugas = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    keterangan = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.get_jenis_transaksi_display()} - {self.aset.nama_barang} ({self.jumlah})"

    class Meta:
        verbose_name = "Transaksi Aset"
        verbose_name_plural = "Riwayat Transaksi Aset"
        ordering = ['-tanggal']
