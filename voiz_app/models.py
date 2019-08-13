from django.db import models
from django import forms
from django.contrib.postgres.fields import ArrayField
from jsonfield import JSONField


class Customer5(models.Model):
    PR = 'Prepaid'
    PO = 'Postpaid'
    DO = 'Dongle'
    prepost = ((PR, 'Prepaid'), (PO, 'Postpaid'), (DO, 'Dongle'))

    p1 = 'Plan 1'
    p2 = 'Plan 2'
    p3 = 'Plan 3'
    planselection = ((p1, 'Plan 1'), (p2, 'Plan 2'), (p3, 'Plan 3'))

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    pincode = models.IntegerField()
    aadhar = models.CharField(max_length=100)
    aadhar_verified = models.BooleanField()
    email = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=10)
    type1 = models.CharField(max_length=8, choices=prepost)
    plan = models.CharField(max_length=10, choices=planselection)
    kyc_date = models.DateField()

    balance = models.CharField(max_length=50)
    # presentPack = models.CharField(max_length=100)
    expiriesIn = models.CharField(max_length=100)
    callUsage = models.CharField(max_length=500)#(9092564782,10/08/19,10min);(9898989898,11/08/19,12min)
    dataUsage = models.CharField(max_length=500)#(10/08/19,10Mb);(11/08/19,11Mb)
    smsUsage = models.CharField(max_length=500)#(9092564782,10/08/19,10);(9092464782,11/08/19,15)
    bill = models.CharField(max_length=2000)#(9873547692,74968736,20-06-2019,15-07-2019 to 20-07-2019,30-07-2019,Rs.300,0);(9873547692,74968736,20-05-2019,15-07-2019 to 20-07-2019,30-07-2019,Rs.200,1)

    def __str__(self):
        return self.phone_num


class PrepaidPlan(models.Model):
    plan_name = models.CharField(max_length=100)
    amount = models.IntegerField()
    duration = models.CharField(max_length=200)
    talktime = models.CharField(max_length=200)
    data = models.CharField(max_length=200)
    sms = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.plan_name


class PostpaidPlan(models.Model):
    plan_name = models.CharField(max_length=100)
    amount = models.IntegerField()
    duration = models.CharField(max_length=200)
    talktime = models.CharField(max_length=200)
    data = models.CharField(max_length=200)
    sms = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.plan_name


class Dongle5(models.Model):
    # PR = 'PR'
    # PO = 'PO'
    # typ = ((PR, 'Prepaid'), (PO, 'Postpaid'))
    plan_name = models.CharField(max_length=100)
    amount = models.IntegerField()
    data = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    # types = models.CharField(max_length=50, choices=typ)

    def __str__(self):
        return self.plan_name


class Plan1(models.Model):
    packname = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    Validity = models.CharField(max_length=100)
    Data = models.CharField(max_length=100)
    Calls = models.CharField(max_length=100)


class MyDBArray(models.Model):
    array_data = models.CharField(max_length=200)
