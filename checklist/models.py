from django.db import models
from django.utils import timezone
from django.conf import settings

class PenerimaanLinen(models.Model):
    class PilihanRuangan(models.TextChoices):
        KAMAR_BEDAH = 'Kamar Bedah', 'Kamar Bedah'
        RAWAT_INAP = 'Rawat Inap', 'Rawat Inap'
        RAWAT_JALAN = 'Rawat Jalan', 'Rawat Jalan'
        IGD = 'IGD', 'IGD'
        PENUNJANG_MEDIS = 'Penunjang Medis', 'Penunjang Medis'
        FASILITAS_UMUM = 'Fasilitas Umum', 'Fasilitas Umum'
        LAINNYA = 'Lainnya', 'Lainnya'

    tanggal = models.DateField(default=timezone.now, verbose_name="Tanggal Penerimaan")
    jam = models.TimeField(default=timezone.now, verbose_name="Jam Penerimaan")
    ruangan = models.CharField(
        max_length=100,
        choices=PilihanRuangan.choices,
        verbose_name="Ruangan/Asal Linen"
    )
    petugas = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.PROTECT, 
        verbose_name="Petugas Penerima"
    )
    dibuat_pada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Penerimaan dari {self.ruangan} - {self.tanggal.strftime('%d %b %Y')}"

    class Meta:
        verbose_name = "Penerimaan Linen"
        verbose_name_plural = "Daftar Penerimaan Linen"
        ordering = ['-tanggal', '-jam']

class ItemLinen(models.Model):
    class PilihanItem(models.TextChoices):
        BAJU_PERAWAT = 'Baju Perawat', 'Baju Perawat'
        BAJU_DOKTER = 'Baju Dokter', 'Baju Dokter'
        BAJU_PASIEN = 'Baju Pasien', 'Baju Pasien'
        BAJU_CLEANER = 'Baju Cleaner', 'Baju Cleaner'
        DOEK_BESAR = 'Doek Besar', 'Doek Besar'
        DOEK_KECIL = 'Doek Kecil', 'Doek Kecil'
        HANDUK_KECIL = 'Handuk Kecil', 'Handuk Kecil'
        LAKEN = 'Laken', 'Laken'
        SARUNG_BANTAL = 'Sarung Bantal', 'Sarung Bantal'
        SELIMUT = 'Selimut', 'Selimut'
        HANDUK = 'Handuk', 'Handuk'
        KESET = 'Keset', 'Keset'
        GOWN = 'Gown Scrub', 'Gown Scrub'
        MUKENA = 'Mukena', 'Mukena'
        SEJADAH = 'Sejadah', 'Sejadah'
        BEDSET = 'Bedset', 'Bedset'
        GORDEN = 'Gorden', 'Gorden'

    class PilihanKondisi(models.TextChoices):
        BAIK = 'Baik', 'Baik'
        NODA = 'Noda', 'Noda'
        RUSAK = 'Rusak', 'Rusak'

    penerimaan = models.ForeignKey(
        PenerimaanLinen, 
        on_delete=models.CASCADE, 
        related_name='items'
    )
    nama_item = models.CharField(
        max_length=100, 
        choices=PilihanItem.choices, 
        verbose_name="Nama Item"
    )
    jumlah = models.PositiveIntegerField(default=1, verbose_name="Jumlah")
    kondisi = models.CharField(
        max_length=10, 
        choices=PilihanKondisi.choices, 
        default=PilihanKondisi.BAIK,
        verbose_name="Kondisi"
    )
    keterangan = models.CharField(max_length=255, blank=True, verbose_name="Keterangan")

    def __str__(self):
        return self.nama_item

    class Meta:
        verbose_name = "Item Linen"
        verbose_name_plural = "Daftar Item Linen"

class BeratLinenHarian(models.Model):
    """
    Model untuk mencatat total berat linen kotor harian per ruangan.
    """
    # == PENAMBAHAN PILIHAN SHIFT ==
    class PilihanShift(models.TextChoices):
        SHIFT_1 = 'Shift 1', 'Shift 1'
        SHIFT_2 = 'Shift 2', 'Shift 2'
        SHIFT_3 = 'Shift 3', 'Shift 3'

    tanggal = models.DateField(verbose_name="Tanggal")
    ruangan = models.CharField(
        max_length=100,
        choices=PenerimaanLinen.PilihanRuangan.choices,
        verbose_name="Ruangan"
    )
    # == PENAMBAHAN FIELD SHIFT ==
    shift = models.CharField(
        max_length=10,
        choices=PilihanShift.choices,
        default=PilihanShift.SHIFT_1,
        verbose_name="Shift"
    )
    total_berat = models.DecimalField(
        max_digits=7, 
        decimal_places=2, 
        verbose_name="Total Berat (Kg)"
    )
    petugas = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT
    )
    dibuat_pada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Berat linen dari {self.get_ruangan_display()} pada {self.tanggal} ({self.shift})"

    class Meta:
        verbose_name = "Berat Linen Harian"
        verbose_name_plural = "Data Berat Linen Harian"
        ordering = ['-tanggal', 'ruangan', 'shift']
