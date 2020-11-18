from django.db import models


class DataTrigrs(models.Model):
    key_id = models.IntegerField(
        default=None, null=False, blank=False, unique=True)
    data_name = models.TextField(default=None, null=False)

    def __str__(self):
        return self.key_id

    class Meta:
        verbose_name = "Data Trigrs"
        verbose_name_plural = "Data Trigrs"


class DataTrigrsDetail(models.Model):
    trigrs = models.ForeignKey(
        DataTrigrs, null=True, on_delete=models.CASCADE, related_name='data_trigrs_detail')
    data_added = models.DateTimeField(
        null=False, auto_now_add=True, editable=False)
    data_updated = models.DateTimeField(
        null=True, blank=True, auto_now_add=True, editable=False)
    ch = models.TextField(default=None, null=True, blank=True)
    filename = models.TextField(default=None, null=False, blank=False)
    file_upload_status = models.TextField(
        default=None, null=False, blank=False)

    def __str__(self):
        return self.trigrs.key_id

    class Meta:
        verbose_name = "Data Trigrs Detail"
        verbose_name_plural = "Data Trigrs Detail"
