from django.db import models

class Bcast(models.Model):
    rowid = models.AutoField(primary_key=True)
    logtype = models.CharField(max_length=32)
    usagetype = models.CharField(max_length=64)
    cnt_globe = models.IntegerField(null=True, blank=True)
    cnt_smart = models.IntegerField(null=True, blank=True)
    cnt_sun = models.IntegerField(null=True, blank=True)
    cnt_unknown = models.IntegerField(null=True, blank=True)
    val_origin = models.CharField(max_length=32, null=True, blank=True)
    trandate = models.CharField(max_length=16)
    tstamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ' '.join([self.logtype, self.usagetype])

    class Meta:
        db_table = "ord_bcast_values"
        managed = False


class Usagetypes(models.Model):
    rowid = models.AutoField(primary_key=True)
    usagetype = models.CharField(max_length=64)

    def __str__(self):
        return ' '.join(self.usagetype)

    class Meta:
        db_table = "ord_usagetypes"
        managed = False

class Dashboard(models.Model):
    rowid = models.AutoField(primary_key=True)
    usagetype = models.CharField(max_length=32)
    daterange_start = models.CharField(max_length=10)
    daterange_end = models.CharField(max_length=10)
    username = models.CharField(max_length=150)
    tstamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.usagetype
    
    def __str__(self):
        return self.usagetype

    class Meta:
        db_table = "ord_bcast_saved_dashboard"
        managed = False

class DashboardLastSession(models.Model):
    rowid = models.AutoField(primary_key=True)
    usagetypelist = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    def __unicode__(self):
        return self.usagetypelist
        
    def __str__(self):
        return self.usagetypelist
        
    class Meta:
        db_table = "ord_bcast_dashboard_last_session"
        