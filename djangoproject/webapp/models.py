from django.db import models

# Create your models here.
class Plans(models.Model):
    plan_id = models.CharField(max_length = 6, primary_key=True)
    free_talktime = models.IntegerField()
    free_sms = models.IntegerField()
    free_data = models.IntegerField()
    call_rate = models.IntegerField()
    sms_rate = models.DecimalField(decimal_places=2, max_digits=30)
    data_rate = models.DecimalField(decimal_places=2, max_digits=30)
    price = models.DecimalField(decimal_places=2, max_digits=30)

class UserDetails(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=45)
    dob = models.DateField()
    phone = models.CharField(max_length=10)
    plan = models.ForeignKey(Plans, on_delete=models.CASCADE, default="INT600")

class UsageDetails(models.Model):
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    call_amount = models.DecimalField(decimal_places=2, max_digits=30)
    sms_amount = models.DecimalField(decimal_places=2, max_digits=30)
    data_amount = models.DecimalField(decimal_places=2, max_digits=30)
    total_amount = models.DecimalField(decimal_places=2, max_digits=30)

class CallsLog(models.Model):
    call_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    call_start = models.TimeField()
    call_end = models.TimeField()

class SmsLog(models.Model):
    sms_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    message_time = models.TimeField()

class DataLog(models.Model):
    data_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    usage_time = models.TimeField()
    data_used = models.DecimalField(decimal_places=2, max_digits=30)