from django.db import models
from django.conf import settings
from django.utils import timezone

class Tugas(models.Model):
    """
    Model untuk menyimpan setiap tugas atau rencana kerja.
    """
    class PilihanStatus(models.TextChoices):
        BELUM_MULAI = 'Belum Dikerjakan', 'Belum Dikerjakan'
        DIKERJAKAN = 'Sedang Dikerjakan', 'Sedang Dikerjakan'
        SELESAI = 'Selesai', 'Selesai'

    class PilihanMinggu(models.TextChoices):
        MINGGU_1 = 'Minggu ke-1', 'Minggu ke-1'
        MINGGU_2 = 'Minggu ke-2', 'Minggu ke-2'
        MINGGU_3 = 'Minggu ke-3', 'Minggu ke-3'
        MINGGU_4 = 'Minggu ke-4', 'Minggu ke-4'

    judul = models.CharField(max_length=200, verbose_name="Pekerjaan")
    deskripsi = models.TextField(blank=True, null=True, verbose_name="Deskripsi")
    status = models.CharField(
        max_length=20,
        choices=PilihanStatus.choices,
        default=PilihanStatus.BELUM_MULAI,
        verbose_name="Status"
    )
    penanggung_jawab = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tugas'
    )
    target_waktu = models.CharField(
        max_length=20,
        choices=PilihanMinggu.choices,
        default=PilihanMinggu.MINGGU_1,
        verbose_name="Target Waktu"
    )
    
    periode = models.CharField(max_length=50, blank=True, null=True, verbose_name="waktu")
    dibuat_pada = models.DateTimeField(auto_now_add=True)
    diperbarui_pada = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.judul

    class Meta:
        verbose_name = "Tugas"
        verbose_name_plural = "Daftar Tugas"
        ordering = ['target_waktu']
