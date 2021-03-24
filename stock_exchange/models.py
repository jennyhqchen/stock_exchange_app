from django.db import models


# Create your models here.
class Stock(models.Model):
    code = models.CharField(primary_key=True, max_length=128)
    code_name = models.CharField(max_length=128)


class K_Day(models.Model):
    code = models.CharField(primary_key=True, max_length=128)
    code_name = models.CharField(max_length=128)
    date = models.CharField(max_length=128)
    open = models.CharField(max_length=128)
    high = models.CharField(max_length=128)
    low = models.CharField(max_length=128)
    close = models.CharField(max_length=128)
    preclose = models.CharField(max_length=128)
    volume = models.CharField(max_length=128)
    amount = models.CharField(max_length=128)
    adjustflag = models.CharField(max_length=128)
    turn = models.CharField(max_length=128)
    tradestatus = models.CharField(max_length=128)
    pctChg = models.CharField(max_length=128)
    isST = models.CharField(max_length=128)


class Order(models.Model):
    username = models.CharField(max_length=128)
    code = models.CharField(max_length=128)
    code_name = models.CharField(max_length=128)
    volume = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sell_or_buy = models.IntegerField(default=0)
    status = models.CharField(max_length=128)


class ShareHolding(models.Model):
    username = models.CharField(max_length=128)
    code = models.CharField(max_length=128)
    code_name = models.CharField(max_length=128)
    volume = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    sell_price = models.DecimalField(max_digits=10, decimal_places=2)
    profit = models.DecimalField(max_digits=10, decimal_places=2)
