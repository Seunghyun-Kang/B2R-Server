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

class CompanyInfoNASDAQ(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    company = models.CharField(max_length=40, blank=True, null=True)
    last_update = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_info_usa'
        unique_together = (('code', 'company'),)

class CompanyInfoCOIN(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    company = models.CharField(max_length=40, blank=True, null=True)
    last_update = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ticker_info'
        unique_together = (('code', 'company'),)

class CompanyInfoCHINA(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    company = models.CharField(max_length=40, blank=True, null=True)
    ticker = models.CharField(max_length=10, blank=True, null=True)
    last_update = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_info_china'
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

class DailyPriceUSA(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    date = models.DateField()
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    diff = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daily_price_usa'

class DailyPriceCHINA(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    date = models.DateField()
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    diff = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daily_price_china'

class DailyPriceCOIN(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    date = models.DateField()
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daily_price_coin'

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

class BollingerInfoUSA(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    date = models.DateField()
    ma20 = models.FloatField(blank=True, null=True)
    stddev = models.FloatField(blank=True, null=True)
    upper = models.FloatField(blank=True, null=True)
    lower = models.FloatField(blank=True, null=True)
    pb = models.FloatField(blank=True, null=True)
    bandwidth = models.FloatField(blank=True, null=True)
    mfi10 = models.FloatField(blank=True, null=True)
    iip21 = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'bollinger_info_usa'

class BollingerInfoCHINA(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    date = models.DateField()
    ma20 = models.FloatField(blank=True, null=True)
    stddev = models.FloatField(blank=True, null=True)
    upper = models.FloatField(blank=True, null=True)
    lower = models.FloatField(blank=True, null=True)
    pb = models.FloatField(blank=True, null=True)
    bandwidth = models.FloatField(blank=True, null=True)
    mfi10 = models.FloatField(blank=True, null=True)
    iip21 = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'bollinger_info_china'

class BollingerInfoCOIN(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    date = models.DateField()
    ma20 = models.FloatField(blank=True, null=True)
    stddev = models.FloatField(blank=True, null=True)
    upper = models.FloatField(blank=True, null=True)
    lower = models.FloatField(blank=True, null=True)
    pb = models.FloatField(blank=True, null=True)
    bandwidth = models.FloatField(blank=True, null=True)
    mfi10 = models.FloatField(blank=True, null=True)
    iip21 = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'bollinger_info_coin'
class BollingerTrendSignal(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    date = models.DateField()
    type = models.CharField(max_length=20, blank=True, null=True)
    close = models.BigIntegerField(blank=True, null=True)
    valid = models.CharField(blank=True, null=True,  max_length=10)
    last_buy_close = models.BigIntegerField(blank=True, null=True)
    last_buy_date = models.DateField()
    last_sell_close = models.BigIntegerField(blank=True, null=True)
    last_sell_date = models.DateField()
    first_buy_date =  models.DateField()
    _period_latest = models.IntegerField(blank=True, null=True)
    _rank = models.IntegerField(blank=True, null=True)
    _returns = models.FloatField(blank=True, null=True)
    _period_first = models.IntegerField(blank=True, null=True)
    buy_count = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'signal_bollinger_trend'

class BollingerTrendSignalUSA(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    date = models.DateField()
    type = models.CharField(max_length=20, blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    valid = models.CharField(blank=True, null=True,  max_length=10)
    last_buy_close = models.FloatField(blank=True, null=True)
    last_buy_date = models.DateField()
    last_sell_close = models.FloatField(blank=True, null=True)
    last_sell_date = models.DateField()
    first_buy_date =  models.DateField()
    _period_latest = models.IntegerField(blank=True, null=True)
    _rank = models.IntegerField(blank=True, null=True)
    _returns = models.FloatField(blank=True, null=True)
    _period_first = models.IntegerField(blank=True, null=True)
    buy_count = models.IntegerField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'signal_bollinger_trend_usa'

class BollingerTrendSignalUSA(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    date = models.DateField()
    type = models.CharField(max_length=20, blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    valid = models.CharField(blank=True, null=True,  max_length=10)
    last_buy_close = models.FloatField(blank=True, null=True)
    last_buy_date = models.DateField()
    last_sell_close = models.FloatField(blank=True, null=True)
    last_sell_date = models.DateField()
    first_buy_date =  models.DateField()
    _period_latest = models.IntegerField(blank=True, null=True)
    _rank = models.IntegerField(blank=True, null=True)
    _returns = models.FloatField(blank=True, null=True)
    _period_first = models.IntegerField(blank=True, null=True)
    buy_count = models.IntegerField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'signal_bollinger_trend_usa'
        
class BollingerTrendSignalCHINA(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    date = models.DateField()
    type = models.CharField(max_length=20, blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    valid = models.CharField(blank=True, null=True,  max_length=10)
    last_buy_close = models.FloatField(blank=True, null=True)
    last_buy_date = models.DateField()
    last_sell_close = models.FloatField(blank=True, null=True)
    last_sell_date = models.DateField()
    first_buy_date =  models.DateField()
    _period_latest = models.IntegerField(blank=True, null=True)
    _rank = models.IntegerField(blank=True, null=True)
    _returns = models.FloatField(blank=True, null=True)
    _period_first = models.IntegerField(blank=True, null=True)
    buy_count = models.IntegerField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'signal_bollinger_trend_china'

class BollingerTrendSignalCOIN(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    date = models.DateField()
    type = models.CharField(max_length=20, blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    valid = models.CharField(blank=True, null=True,  max_length=10)
    last_buy_close = models.FloatField(blank=True, null=True)
    last_buy_date = models.DateField()
    last_sell_close = models.FloatField(blank=True, null=True)
    last_sell_date = models.DateField()
    
    class Meta:
        managed = False
        db_table = 'signal_bollinger_trend_coin'
        
class BollingerReverseSignal(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    date = models.DateField()
    type = models.CharField(max_length=20, blank=True, null=True)
    close = models.BigIntegerField(blank=True, null=True)
    valid = models.CharField(blank=True, null=True, max_length=10)
    last_buy_close = models.BigIntegerField(blank=True, null=True)
    last_buy_date = models.DateField()
    last_sell_close = models.BigIntegerField(blank=True, null=True)
    last_sell_date = models.DateField()
    first_buy_date =  models.DateField()
    _period_latest = models.IntegerField(blank=True, null=True)
    _rank = models.IntegerField(blank=True, null=True)
    _returns = models.FloatField(blank=True, null=True)
    _period_first = models.IntegerField(blank=True, null=True)
    buy_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'signal_bollinger_reverse'
class BollingerTest1Signal(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    date = models.DateField()
    type = models.CharField(max_length=20, blank=True, null=True)
    close = models.BigIntegerField(blank=True, null=True)
    valid = models.CharField(blank=True, null=True, max_length=10)
    last_buy_close = models.BigIntegerField(blank=True, null=True)
    last_buy_date = models.DateField()
    last_sell_close = models.BigIntegerField(blank=True, null=True)
    last_sell_date = models.DateField()
    first_buy_date =  models.DateField()
    _period_latest = models.IntegerField(blank=True, null=True)
    _rank = models.IntegerField(blank=True, null=True)
    _returns = models.FloatField(blank=True, null=True)
    _period_first = models.IntegerField(blank=True, null=True)
    buy_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'signal_test_algorithm1'

class BollingerTest2Signal(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    date = models.DateField()
    type = models.CharField(max_length=20, blank=True, null=True)
    close = models.BigIntegerField(blank=True, null=True)
    valid = models.CharField(blank=True, null=True, max_length=10)
    last_buy_close = models.BigIntegerField(blank=True, null=True)
    last_buy_date = models.DateField()
    last_sell_close = models.BigIntegerField(blank=True, null=True)
    last_sell_date = models.DateField()
    first_buy_date =  models.DateField()
    _period_latest = models.IntegerField(blank=True, null=True)
    _rank = models.IntegerField(blank=True, null=True)
    _returns = models.FloatField(blank=True, null=True)
    _period_first = models.IntegerField(blank=True, null=True)
    buy_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'signal_test_algorithm2'

class BollingerReverseSignalUSA(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    date = models.DateField()
    type = models.CharField(max_length=20, blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    valid = models.CharField(blank=True, null=True, max_length=10)
    last_buy_close = models.FloatField(blank=True, null=True)
    last_buy_date = models.DateField()
    last_sell_close = models.FloatField(blank=True, null=True)
    last_sell_date = models.DateField()
    first_buy_date =  models.DateField()
    _period_latest = models.IntegerField(blank=True, null=True)
    _rank = models.IntegerField(blank=True, null=True)
    _returns = models.FloatField(blank=True, null=True)
    _period_first = models.IntegerField(blank=True, null=True)
    buy_count = models.IntegerField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'signal_bollinger_reverse_usa'

class BollingerReverseSignalCHINA(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    date = models.DateField()
    type = models.CharField(max_length=20, blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    valid = models.CharField(blank=True, null=True, max_length=10)
    last_buy_close = models.FloatField(blank=True, null=True)
    last_buy_date = models.DateField()
    last_sell_close = models.FloatField(blank=True, null=True)
    last_sell_date = models.DateField()
    first_buy_date =  models.DateField()
    _period_latest = models.IntegerField(blank=True, null=True)
    _rank = models.IntegerField(blank=True, null=True)
    _returns = models.FloatField(blank=True, null=True)
    _period_first = models.IntegerField(blank=True, null=True)
    buy_count = models.IntegerField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'signal_bollinger_reverse_china'

class BollingerReverseSignalCOIN(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    date = models.DateField()
    type = models.CharField(max_length=20, blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    valid = models.CharField(blank=True, null=True, max_length=10)
    last_buy_close = models.FloatField(blank=True, null=True)
    last_buy_date = models.DateField()
    last_sell_close = models.FloatField(blank=True, null=True)
    last_sell_date = models.DateField()
    
    class Meta:
        managed = False
        db_table = 'signal_bollinger_reverse_coin'

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

class TripleScreenInfoUSA(models.Model):
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
        db_table = 'tripplescreen_info_usa'

class TripleScreenInfoCOIN(models.Model):
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
        db_table = 'tripplescreen_info_coin'

class TripleScreenSignal(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    date = models.DateField()
    type = models.CharField(max_length=20, blank=True, null=True)
    close = models.BigIntegerField(blank=True, null=True)
    valid = models.CharField(blank=True, null=True, max_length=10)
    last_buy_close = models.BigIntegerField(blank=True, null=True)
    last_buy_date = models.DateField()
    last_sell_close = models.BigIntegerField(blank=True, null=True)
    last_sell_date = models.DateField()
    
    class Meta:
        managed = False
        db_table = 'signal_tripplescreen'

class TripleScreenSignalUSA(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    date = models.DateField()
    type = models.CharField(max_length=20, blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    valid = models.CharField(blank=True, null=True, max_length=10)
    last_buy_close = models.FloatField(blank=True, null=True)
    last_buy_date = models.DateField()
    last_sell_close = models.FloatField(blank=True, null=True)
    last_sell_date = models.DateField()
    
    class Meta:
        managed = False
        db_table = 'signal_tripplescreen_usa'

class TripleScreenSignalCOIN(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    date = models.DateField()
    type = models.CharField(max_length=20, blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    valid = models.CharField(blank=True, null=True, max_length=10)
    last_buy_close = models.FloatField(blank=True, null=True)
    last_buy_date = models.DateField()
    last_sell_close = models.FloatField(blank=True, null=True)
    last_sell_date = models.DateField()
    
    class Meta:
        managed = False
        db_table = 'signal_tripplescreen_coin'

class Momentum(models.Model):
    hashcode = models.CharField(primary_key=True, max_length=20)
    date = models.DateField()
    company = models.CharField(max_length=100, blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    returns = models.FloatField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'momentum'

class TradeHistory(models.Model):
    hashcode = models.CharField(primary_key=True, max_length=20)
    id = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField()
    code = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'trade_history'

class FearAndGreedIndexUSA(models.Model):
    date = models.DateField(primary_key=True)
    now_value = models.IntegerField(blank=True, null=True)
    week_ago_value = models.IntegerField(blank=True, null=True)
    month_ago_value = models.IntegerField(blank=True, null=True)
    year_ago_value = models.IntegerField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'fear_and_greed_index_usa'