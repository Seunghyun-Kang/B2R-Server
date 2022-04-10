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

class BollingerInfo(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    date = models.DateField()
    ma20 = models.FloatField(blank=True, null=True)
    stddev = models.FloatField(blank=True, null=True)
    upper = models.BigIntegerField(blank=True, null=True)
    lower = models.BigIntegerField(blank=True, null=True)
    pb = models.FloatField(blank=True, null=True)
    bandwidth = models.FloatField(blank=True, null=True)
    mfi10 = models.FloatField(blank=True, null=True)
    iip21 = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'bollinger_info'

class BollingerTrendSignal(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    date = models.DateField()
    type = models.CharField(max_length=20, blank=True, null=True)
    close = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'signal_bollinger_trend'

class BollingerReverseSignal(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    date = models.DateField()
    type = models.CharField(max_length=20, blank=True, null=True)
    close = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'signal_bollinger_reverse'

class TripleScreenInfo(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    date = models.DateField()
    ema130 = models.FloatField(blank=True, null=True)
    ema60 = models.FloatField(blank=True, null=True)
    macd = models.FloatField(blank=True, null=True)
    _signal = models.FloatField(blank=True, null=True)
    macdhist = models.FloatField(blank=True, null=True)
    fast_k = models.FloatField(blank=True, null=True)
    slow_d = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'tripplescreen_info'

class TripleScreenSignal(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    date = models.DateField()
    type = models.CharField(max_length=20, blank=True, null=True)
    close = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'signal_tripplescreen'
