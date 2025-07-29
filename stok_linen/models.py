from django.db import models
from django.conf import settings
from checklist.models import PenerimaanLinen, ItemLinen

class StokLinen(models.Model):
    """
    Model untuk menyimpan data master stok linen per ruangan.
    Setiap kombinasi ruangan dan nama linen harus unik.
    """
    nama_linen = models.CharField(
        max_length=100,
        choices=ItemLinen.PilihanItem.choices,
        verbose_name="Nama Linen"
    )
    ruangan = models.CharField(
        max_length=100,
        choices=PenerimaanLinen.PilihanRuangan.choices,
        verbose_name="Ruangan"
    )
    stok_akhir = models.PositiveIntegerField(default=0, verbose_name="Stok Akhir")
    keterangan = models.TextField(blank=True, null=True)
    update_terakhir = models.DateTimeField(auto_now=True, verbose_name="Update Terakhir")

    def __str__(self):
        return f"{self.get_nama_linen_display()} - Ruangan: {self.get_ruangan_display()}"

    class Meta:
        verbose_name = "Stok Linen"
        verbose_name_plural = "Daftar Stok Linen"
        ordering = ['ruangan', 'nama_linen']
        unique_together = ('nama_linen', 'ruangan')

class TransaksiLinen(models.Model):
    """
    Model untuk mencatat setiap transaksi linen (masuk atau keluar).
    """
    class PilihanTransaksi(models.TextChoices):
        MASUK = 'MASUK', 'Linen Masuk'
        KELUAR = 'KELUAR', 'Linen Keluar'

    stok_linen = models.ForeignKey(StokLinen, on_delete=models.PROTECT, related_name='transaksi', verbose_name="Item Linen")
    jenis_transaksi = models.CharField(max_length=10, choices=PilihanTransaksi.choices, verbose_name="Jenis Transaksi")
    jumlah = models.PositiveIntegerField()
    tanggal = models.DateField(verbose_name="Tanggal Transaksi")
    petugas = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    keterangan = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.get_jenis_transaksi_display()} - {self.stok_linen.nama_linen} ({self.jumlah})"

    class Meta:
        verbose_name = "Transaksi Linen"
        verbose_name_plural = "Riwayat Transaksi Linen"
        ordering = ['-tanggal']
