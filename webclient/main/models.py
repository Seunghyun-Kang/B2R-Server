from django.db import models

# Create your models here.
class AllCompanies(models.Model):
    code = models.CharField(max_length=20)
    company = models.CharField(max_length=40, blank=True, null=True)
    last_update = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_info'

class CompanyInfo(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    company = models.CharField(max_length=40, blank=True, null=True)
    last_update = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_info'
        unique_together = (('code', 'company'),)


class DailyPrice(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    date = models.DateField()
    open = models.BigIntegerField(blank=True, null=True)
    high = models.BigIntegerField(blank=True, null=True)
    low = models.BigIntegerField(blank=True, null=True)
    close = models.BigIntegerField(blank=True, null=True)
    diff = models.BigIntegerField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daily_price'
