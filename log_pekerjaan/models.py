from django.db import models
from django.conf import settings
from django.utils import timezone

class LogPekerjaan(models.Model):
    tanggal = models.DateField(
        default=timezone.localdate, 
        verbose_name="Tanggal"
    )
    keterangan = models.TextField(
        verbose_name="Keterangan Catatan / Kejadian"
    )
    # PJ otomatis mengambil user yang login
    pj = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.PROTECT, 
        verbose_name="Penanggung Jawab (PJ)"
    )
    dibuat_pada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Log {self.tanggal} - {self.pj.username}"

    class Meta:
        verbose_name = "Log Pekerjaan"
        verbose_name_plural = "Daftar Log Pekerjaan"
        ordering = ['-tanggal', '-dibuat_pada']